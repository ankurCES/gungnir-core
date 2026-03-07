# DEVELOPMENT_STANDARDS.md

## Repository Structure
- All repositories MUST include `ABOUT_DEVELOPER.md`.
- All code MUST include detailed docstrings and "Why" comments.
- **Developer Name:** Ankur Nair
- **LinkedIn Profile:** [Ankur Nair](https://www.linkedin.com/in/ankur-nair-10baab350?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

## Commit Guidelines
- Commit at least once every **30 minutes**.
- Meaningful commit messages are mandatory.
- **Mandatory Notification Format:** Every module or feature committed must be reported to Odin in the following format:
  1. Repository Name
  2. Summary of module/feature
  3. Link to commit or branch (if available)
  4. The **"Why"** behind the module.

## Visual Evidence: Recording Protocol
- **Browser-Based Execution:** Every module's visual evidence MUST be captured by running the developed tool interface directly in a browser.
- **Proper Demo Elements:** The recording must use realistic demo elements, mock data, and proper user interactions to demonstrate the module's "mission."
- **Repository Persistence:** The screen recording must be saved *within the repository* (e.g., in `/docs/evidence/` or `/assets/`).
- **Display:** These recordings must be embedded in the repository `README.md` and showcased on the GitHub.io site for each module.

## Team Responsibilities (Recording)
- **Qin Shi Huang (Lead):** Responsible for delivering the functional interface for recording.
- **Apollo (Marketing):** Responsible for performing the browser-based recording and integrating it into the showcase.

## Token & Resource Management
- **Efficiency First:** Agents must use the most token-efficient model available for the specific task.
- **Monitoring:** Anubis must track token usage across the sprint and flag any unexpected spikes.
- **System Load Throttling:** If the Jetson system load average exceeds 10.0 or thermals exceed 75°C, the team must immediately pause non-critical background tasks for a 15-minute "Forge Cool-down."

## Team roles:
- **Odin (All-Father):** Workspace orchestrator & Token oversight.
- **Tesla (Architect):** Design and module mapping for the showcase.
- **Qin Shi Huang (Lead):** Technical execution and capturing visual evidence.
- **Apollo (Marketing/Frontend):** Creating the Apple-style GitHub.io showcase site.
- **Anubis (Guardian of the Scales):** Pipeline management & Resource balancing.
- **Valkyrie Assistants:** 
    - **Brunhilde:** Documentation, structure, and metadata support.
    - **Göll:** Testing and refactoring support.
    - **Randgriz:** Environment and CI/CD support.
- **Hamingja Team (Local Backup):**
    - **Thor:** Local backend offloading.
    - **Loki:** Rapid UI tweaks and quick fixes.
