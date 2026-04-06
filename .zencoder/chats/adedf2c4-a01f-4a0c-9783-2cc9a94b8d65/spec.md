# Technical Specification: Skill and Logic Mastery Guide

## Technical Context
- **Language**: Markdown (Vietnamese/English)
- **Target Audience**: Developers looking to improve both logical thinking (DSA) and practical development skills (Fullstack/Odoo/Python).
- **Existing Resources**: `CODE_EXERCISES.md`, `DSA_Giao_Trinh_Chi_Tiet.md`, `Roadmap_Fresher_Junior_RutGon.md`, `ON_LUYEN_PHONG_VAN.md`.

## Implementation Approach
The goal is to create a single entry point file (`SKILL_AND_LOGIC_MASTERY.md`) that synthesizes existing resources into a actionable daily/weekly routine.

### Key Sections:
1. **Daily Routine (The "70/30" Rule)**: 70% Practical Dev, 30% Logic/DSA.
2. **Logic Roadmap**: Structured path from basic to advanced DSA patterns (Sliding Window, Two Pointers, Trees, etc.), linking each to `20_exam_exercies/` or LeetCode.
3. **Dev Roadmap**: Focus on high-impact skills (Clean Code, Design Patterns, Database Optimization, Security) linking to `CODE_EXERCISES.md` and `ON_LUYEN_PHONG_VAN.md`.
4. **The "Bridge" Exercises**: Exercises that require both logic and dev skills (e.g., implementing a custom caching layer, optimizing a complex search query).
5. **Progress Tracking**: A checklist or table for users to track their daily/weekly progress.

## Source Code Structure Changes
- New file: `/home/mbw25/leetcode/repo/SKILL_AND_LOGIC_MASTERY.md`
- No changes to existing source code files (`.py`, `.vue`, etc.) unless specific "Bridge" exercises require them.

## Data Model / API / Interface Changes
- N/A (Markdown only).

## Verification Approach
- **Manual Review**: Ensure all links to existing files are correct.
- **Content Accuracy**: Verify that the suggested routine is realistic and follows the 70/30 rule mentioned in existing roadmaps.
- **Readability**: Ensure the Markdown is well-formatted and easy to navigate.
