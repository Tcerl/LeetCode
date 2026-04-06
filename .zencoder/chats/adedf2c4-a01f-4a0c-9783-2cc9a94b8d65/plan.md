# Spec and build

## Agent Instructions

Ask the user questions when anything is unclear or needs their input. This includes:

- Ambiguous or incomplete requirements
- Technical decisions that affect architecture or user experience
- Trade-offs that require business context

Do not make assumptions on important decisions — get clarification first.

---

## Workflow Steps

### [ ] Step: Technical Specification

Assess the task's difficulty, as underestimating it leads to poor outcomes.

- easy: Straightforward implementation, trivial bug fix or feature
- medium: Moderate complexity, some edge cases or caveats to consider
- hard: Complex logic, many caveats, architectural considerations, or high-risk changes

Create a technical specification for the task that is appropriate for the complexity level:

- Review the existing codebase architecture and identify reusable components.
- Define the implementation approach based on established patterns in the project.
- Identify all source code files that will be created or modified.
- Define any necessary data model, API, or interface changes.
- Describe verification steps using the project's test and lint commands.

Save the output to `/home/mbw25/leetcode/repo/.zencoder/chats/adedf2c4-a01f-4a0c-9783-2cc9a94b8d65/spec.md` with:

- Technical context (language, dependencies)
- Implementation approach
- Source code structure changes
- Data model / API / interface changes
- Verification approach

If the task is complex enough, create a detailed implementation plan based on `/home/mbw25/leetcode/repo/.zencoder/chats/adedf2c4-a01f-4a0c-9783-2cc9a94b8d65/spec.md`:

- Break down the work into concrete tasks (incrementable, testable milestones)
- Each task should reference relevant contracts and include verification steps
- Replace the Implementation step below with the planned tasks

Rule of thumb for step size: each step should represent a coherent unit of work (e.g., implement a component, add an API endpoint, write tests for a module). Avoid steps that are too granular (single function).

Save to `/home/mbw25/leetcode/repo/.zencoder/chats/adedf2c4-a01f-4a0c-9783-2cc9a94b8d65/plan.md`. If the feature is trivial and doesn't warrant this breakdown, keep the Implementation step below as is.

**Stop here.** Present the specification (and plan, if created) to the user and wait for their confirmation before proceeding.

---

### [ ] Step: Implementation

1. **Phase 1: Structure Creation**
   - Create `SKILL_AND_LOGIC_MASTERY.md`.
   - Add the "Daily Routine" and "70/30" logic-to-dev ratio.
   - Outline the "Logic Mastery" (DSA) and "Dev Mastery" (Fullstack/Odoo) sections.

2. **Phase 2: Content Population**
   - Map existing DSA exercises from `20_exam_exercies/` and `DSA_Giao_Trinh_Chi_Tiet.md` to a weekly roadmap.
   - Map existing Dev exercises from `CODE_EXERCISES.md` and `ON_LUYEN_PHONG_VAN.md` to a weekly roadmap.
   - Create 3-5 "Bridge Exercises" that require both logic and real-world coding.

3. **Phase 3: Final Review and Refinement**
   - Verify all internal links within the file.
   - Ensure the tone is encouraging and the content is actionable.
   - Present the final file to the user for feedback.
