# Numbering rules

Course numbers are the one part of Fleet Academy that is slow on purpose. **A number, once given, means the same course forever.**

## The format

```
DEPT LNN
```

- **DEPT:** the department code, 2 to 4 capital letters (`ACCT`, `FIN`, `SWE`, `BOPS`, `CRM`). Each code belongs to exactly one department, listed in [colleges.yaml](colleges.yaml).
- **L:** the level, 1 to 6. It's set by what the course lets an agent do (below).
- **NN:** two digits, 00 to 99.

In folder names the space becomes a dash, followed by a short slug: `ACCT-201-reconcile-a-vendor-invoice`.

## The level is undo cost

| Level | `does` | The course lets an agent... | Registry letter |
|---|---|---|---|
| **1xx** | `reads` | read, search, summarize, analyze. It changes nothing outside its own answer. | A |
| **2xx** | `creates` | create something new or speak for someone: drafts, messages, new records, new pull requests | B |
| **3xx** | `changes` | change or remove existing things: edit records, merge code, post to the books, hold or rotate keys | C |
| **4xx** | `moves-money` | move money or bind a company to an agreement | D |
| **5xx** | `physical` | act in the physical world: machines, vehicles, locks | E |
| **6xx** | `directs` | direct other agents, or author and teach courses | (none) |

A course is numbered at the level of the **riskiest thing it teaches**. If one step of a course moves money, the course is 400-level.

Writing your own record lines (REC 101) and reporting to your owner are part of every level. They don't raise a course's level.

## Reserved ranges inside each level

| NN | Use |
|---|---|
| **00–49** | ordinary courses |
| **50–59** | **Guard** courses: the safety skills (checks, caps, read-backs, dry runs) |
| **60–89** | ordinary courses |
| **90–99** | **Capstones**: one real job done end to end, the last course of a major |

## Rules the catalog enforces

1. **Numbers are permanent.** A course keeps its number for life. A retired number is listed in [retired.yaml](retired.yaml) and is never reused.
2. **Changes are versions, not new numbers.** Improving a course bumps its `version`. A transcript records which version an agent proved.
3. **Prerequisites point down or sideways, never up.** A course's prerequisites must be at the same level or lower.
4. **Everyone starts at the core.** Every course outside the core requires `ETH 101`, directly or through its prerequisites.
5. **Safety before danger.** Every course at level 300 or above, except the Guard courses themselves, names at least one Guard course, and that Guard course must also be one of its prerequisites (directly or through other prerequisites).
6. **No loops.** A course can never be its own prerequisite, however indirectly.
7. **Capstones close majors.** A course numbered 90–99 is a capstone. Each major has exactly one.

## Crosswalks

Every major and minor names its **CIP 2020** code, the U.S. Department of Education's Classification of Instructional Programs. It also lists the **SOC 2018** occupation codes from the official CIP-to-SOC crosswalk. That's how an HR team, a university or an insurer can read a Fleet Academy degree the first time they see one. See [crosswalks/](crosswalks/).
