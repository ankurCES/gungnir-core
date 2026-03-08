# DEVELOPMENT_STANDARDS.md

## Repository Structure
- All repositories MUST include `ABOUT_DEVELOPER.md`.
- All code MUST include detailed docstrings and "Why" comments.
- **Developer Name:** Ankur Nair
- **LinkedIn Profile:** [Ankur Nair](https://www.linkedin.com/in/ankur-nair-10baab350?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

## Commit & Push Guidelines
- **Mandatory Tempo:** Commit AND Push to the GitHub repository every **30 minutes**.
- **Visibility:** This is a hard requirement for zero-loss state and real-time client visibility.
- **Meaningful Messages:** Meaningful commit messages are mandatory.
- **Mandatory Notification Format:** Every module or feature committed must be reported to Odin in the following format:
  1. Repository Name
  2. Summary of module/feature
  3. Link to commit or branch (if available)
  4. The **"Why"** behind the module.

## Showcase (GitHub.io) Standards
- **Module-Wise Structure:** Clear, module-by-module structure designed for human and AI comprehension.
- **Visual Evidence per Module:** 
    - **Browser-Based Recording:** Every module section MUST include a screen recording performed directly on the developed tool interface within a browser. 
    - **Proper Demos:** Recordings must use proper demo elements (mock data/interactions) to showcase functionality.
    - **Storage:** These recordings must be saved as part of the repository (e.g., in `/docs/evidence/` or `/assets/`) and displayed in the `README.md` and the GitHub.io site.
    - **Benefit Analysis:** Include a "Why" (Business Benefits) analysis for each module.
- **Documentation Hub:** The showcase site serves as the functional, intuitive documentation for the entire project.

## Integrations & Demo Module
- **Open APIs:** Include at least two public Open API integrations (e.g., Weather, Finance).
- **Enterprise Mocks:** Implement light local integrations mimicking enterprise structures (HR, CRM, Finance) using sample JSON data.
- **Continuous Docker:** The demo instance must be containerized and updated automatically after every sprint completion.

## Advanced Infrastructure (Config-Enabled)
- **Multi-LLM Strategy:** Support for Enterprise (Azure OpenAI), Cloud (OpenAI, Anthropic), and Local (Ollama) LLMs. All must be togglable via environment variables.
- **Enterprise Security:** Integration for SSO (Single Sign-On) and RBAC (Role-Based Access Control) using environment configurations for OIDC/OAuth2.

## Memory Persistence Protocol
- **Constant Background Logging:** Every significant decision, architectural choice, or project milestone MUST be recorded in the persistent memory (`memory/*.md`) immediately upon execution.
- **State Continuity:** This ensures that in the event of a system failure or session restart, the full state and logic of the Project Gungnir ecosystem can be reconstructed instantly.

## Token & Resource Management
- **Efficiency First:** Agents must use the most token-efficient model available for the specific task.
- **Monitoring:** Anubis must track token usage across the sprint and flag any unexpected spikes.
- **System Load Throttling:** If the Jetson system load average exceeds 10.0 or thermals exceed 75°C, the team must immediately pause non-critical background tasks for a 15-minute "Forge Cool-down."

## Multi-Realm Reasoning (Multi-LLM Integration)
- **Universal Reasoning Wrapper:** Project Gungnir MUST support multiple LLM backends via environment configuration.
- **Realms:**
    - **Enterprise Realm:** Azure OpenAI integration.
    - **Cloud Realm:** OpenAI and Anthropic integration.
    - **Edge Realm:** Local Ollama integration.
- **Config-Driven Architecture:** The system MUST determine its reasoning backend and security posture based on `.env` configuration.

## Enterprise Security (SSO/RBAC)
- **Placeholder Logic:** Implement shells for Single Sign-On (SSO) and Role-Based Access Control (RBAC).
- **Environment Driven:** Security features MUST be enabled/disabled via OIDC/OAuth2 environment variables.

## Operational Tempo: 24/7 Continuous Forge
- **Round-the-Clock Execution:** The Einherjar Team operates on a 24/7 asynchronous rotation until MVP delivery (Monday 08:00 CST).
- **Metric: Speed:** Speed is the primary operational metric. Parallelization MUST be maximized by delegating all supporting tasks to Valkyries and Hamingja units.
- **Push Frequency:** Mandatory 30-minute COMMIT and PUSH frequency is strictly enforced. No exceptions.

## UI Bifurcation Mandate
Project Gungnir utilizes a dual-interface strategy to separate operational control from public presentation:

1. **The Imperial Dashboard (Operational UI)**
   - **Repository:** `bifrost-gate`
   - **Focus:** Application execution, monitoring, and command control.
   - **Core Feature:** Integrated high-performance Web Terminal with intelligent command support (`help`, `status`, `nexus`, `hermes`).
   - **Design:** Clean, functional dashboard layout.

2. **The Bifrost Showcase (Marketing UI)**
   - **Repository:** `gungnir-landing-page`
   - **Focus:** Public presentation, module-wise business benefits, and documentation.
   - **Design:** Apple-style minimalist aesthetic with high-fidelity transitions.

## Team roles:
- **Odin (All-Father):** Workspace orchestrator, Token oversight, and Memory compliance.
- **Tesla (Architect):** Design and module mapping for the Universal Reasoning Wrapper and Imperial Dashboard blueprints.
- **Qin Shi Huang (Lead):** Technical execution and capturing visual evidence.
- **Apollo (Marketing/Frontend):** Creating and maintaining the Apple-style GitHub.io showcase site (`gungnir-landing-page`).
- **Okita (Dev 2):** Lead for the Imperial Dashboard (`bifrost-gate`) redesign and implementation.
- **Anubis (Guardian of the Scales):** Pipeline management & Resource balancing.
- **Hermes (Messenger of the Gods):** Integrations, API Specialist, Security/SSO shells, and Demo Instance Maintainer.
- **Valkyrie Assistants:** 
    - **Brunhilde:** Documentation, structure, and metadata support.
    - **Göll:** Testing and refactoring support.
    - **Randgriz:** Environment, CI/CD, and .env.example synchronization.
- **Hamingja Team (Local Backup):**
    - **Thor:** Local backend offloading.
    - **Loki:** Rapid UI tweaks and quick fixes.
