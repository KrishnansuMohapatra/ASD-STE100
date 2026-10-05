"""Objective readability metrics for the three chat-experiment outputs."""
import re

FILES = {
    "Prompt 1 (bare)": "response_prompt1.md",
    "Prompt 2 (simple)": "response_prompt2.md",
    "Prompt 3 (STE+constraints)": "response_prompt3.md",
}


def clean(text: str) -> str:
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        s = re.sub(r"\*\*", "", s)          # bold markers
        s = re.sub(r"^\d+\.\s*", "", s)      # numbered list prefixes
        s = re.sub(r"^-\s*", "", s)          # bullet prefixes
        lines.append(s)
    return " ".join(lines)


def sentences(text: str):
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p for p in (p.strip() for p in parts) if p]


def words(text: str):
    return re.findall(r"[A-Za-z0-9]+(?:[='*./-][A-Za-z0-9]+)*", text)


def syllables(word: str) -> int:
    w = word.lower()
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    return max(1, n)


def flesch(text: str) -> float:
    ws, ss = words(text), sentences(text)
    syl = sum(syllables(w) for w in ws)
    return 206.835 - 1.015 * (len(ws) / len(ss)) - 84.6 * (syl / len(ws))


JARGON = [
    "optimization", "differentiable", "objective function", "gradient", "loss function",
    "parameters", "weights", "biases", "convergence", "converge", "learning rate",
    "stochastic", "mini-batch", "batch", "SGD", "Adam", "RMSProp", "momentum",
    "non-convex", "local minimum", "global minimum", "saddle", "first-order",
    "isotropic", "GPU", "generalization", "feature scaling", "normalization",
    "early stopping", "schedule", "hyperparameter",
]

print(f"{'Metric':<34}{'P1 bare':>16}{'P2 simple':>16}{'P3 STE':>16}")
stats = {}
for label, fname in FILES.items():
    with open(fname) as f:
        text = clean(f.read())
    ss = sentences(text)
    ws = words(text)
    lens = [len(words(s)) for s in ss]
    stats[label] = {
        "words": len(ws),
        "sentences": len(ss),
        "avg_sent_len": sum(lens) / len(lens),
        "max_sent_len": max(lens),
        "over20": sum(1 for l in lens if l > 20),
        "flesch": flesch(text),
        "jargon_hits": sorted({j for j in JARGON if j.lower() in text.lower()}),
    }

rows = [
    ("Words", "words", "{:.0f}"),
    ("Sentences", "sentences", "{:.0f}"),
    ("Avg sentence length (words)", "avg_sent_len", "{:.1f}"),
    ("Longest sentence (words)", "max_sent_len", "{:.0f}"),
    ("Sentences > 20 words", "over20", "{:.0f}"),
    ("Flesch Reading Ease (higher=easier)", "flesch", "{:.1f}"),
]
for name, key, fmt in rows:
    vals = [fmt.format(stats[l][key]) for l in FILES]
    print(f"{name:<34}{vals[0]:>16}{vals[1]:>16}{vals[2]:>16}")

print("\nTechnical-term hits per output:")
for label in FILES:
    print(f"- {label}: {len(stats[label]['jargon_hits'])} -> {', '.join(stats[label]['jargon_hits'])}")
