# 🥐 **LabsBakery** – *“Figma‑for‑Cyber‑Labs”*

> **Status :** ⛔ **Pre‑Alpha (MVP in progress)** – the code is still dough! Expect broken edges.

    

---

## What is it?

Imagine you’re making a **recipe card** for a hacking playground.

1. **Pick ingredients** – grab ready‑made virtual machines (Windows, Kali, Ubuntu…).
2. **Connect them** – draw lines to show who can talk to whom.
3. **Hit Bake** – LabsBakery writes a tiny text file with the instructions.

That text file (just a few KB) is all you share. Your friend opens it, runs one command, and their computer downloads the VMs and builds the **exact same lab**.  No carving up huge disk images, no confusing setup steps—just share the card, and everyone gets the same dish.

---

## Why another tool?

| Pain today                                         | LabsBakery fix                 |
| -------------------------------------------------- | ------------------------------ |
| Copy‑pasting YAML from DetectionLab or AttackRange | Visual builder with undo/redo  |
| VM sprawl and unclear topology                     | Live topology preview          |
| Hard to share labs with students/teammates         | Template gallery (coming v0.4) |

---

## Current status – 2025‑06‑30

* ✅ **Canvas prototype** – move nodes, draw links.
* ✅ Generates **`Vagrantfile`** & JSON state.
* 🔄 **Provider layer** – pinned to **Vagrant ≤ 2.3.7** (MPL‑2.0) while we bake a libvirt/Multipass backend.
* 🔨 *MVP target* (T + 30 days): lifecycle API, undo/redo, tests, docs.

See [`ROADMAP.md`](ROADMAP.md) for milestone details.

---

## Getting started (dev preview)

```bash
# 1. Clone
$ git clone https://github.com/twarga/LabsBakery.git && cd LabsBakery

# 2. Backend
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn app.main:app --reload  # FastAPI

# 3. Front‑end (Tailwind + Alpine.js)
$ npm install && npm run dev

# 4. Open http://localhost:5173  – start baking!
```

> **Heads‑up:** Only Vagrant ≤ 2.3.7 is supported right now:
>
> ```bash
> $ vagrant --version  # expect 2.3.x
> ```

Full install guide will ship with **v0.3.0**.

---

## Roadmap (high‑level)

| Version         | Planned highlights                                             |
| --------------- | -------------------------------------------------------------- |
| **0.3.0 – MVP** | Lifecycle API, undo/redo, unit tests, README quick‑start       |
| **0.4.0**       | Public box registry, template gallery, Multipass backend       |
| **0.5.0**       | Classroom roles, per‑user lab instances, flag grading          |
| **1.0.0**       | Stable API, provider plugins, cloud offering (**BakeryCloud**) |

Detailed tasks live in [GitHub Projects](../../projects).

---

## Contributing – *soft‑open*

\:hand: **We’re not accepting big features yet.** Until 0.3 lands, we *love*:

* Docs fixes / typos 📝
* Reproducible bug reports 🐞
* Test cases ✅

When the MVP ships we’ll open broader PRs.  See [`CONTRIBUTING.md`](CONTRIBUTING.md) (coming soon).

---

## License

This repository is **AGPL‑3.0‑or‑later**. That means:

* Free for personal & commercial use **as long as any public deployment also shares its source**.
* Need a closed‑source exception? → email [labsbakery@twarga.dev](mailto:labsbakery@twarga.dev).

---

## Community & Support

* **Discussions** – [https://github.com/twarga/LabsBakery/discussions](https://github.com/twarga/LabsBakery/discussions)
* **Issues** – please search before filing.
* **Twitter/X** – [@twarga](https://twitter.com/twarga) – progress log (#100DaysOfDevSecOps).

Star ★ the repo to follow along – the oven’s just warming up!
