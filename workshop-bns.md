author: GitHub
summary: Bandai Namco Studios GitHub Copilot Hands-on Workshop
id: github-copilot-workshop
categories: AI, Development
environments: Web
status: Published
feedback link: https://example.com/feedback

# Bandai Namco Studios GitHub Copilot Hands-on Workshop

## About This Workshop
Duration: 5

Thank you to everyone at Bandai Namco Studios for joining us today. Welcome to this one-hour hands-on workshop presented directly by GitHub employees.

![GitHub Copilot Logo](github-copilot-workshop/img/octocat_copilot.png)

Although our time is short, our goal is for you to **get hands-on experience with GitHub Copilot**. This workshop is designed to help even those who are not engineers in their day-to-day work develop a practical sense of how to work with AI.

### Today's Goals
- Verify that VS Code, GitHub Copilot CLI, and Copilot App are working
- Understand how to reduce token usage and AI Credits
- Use **Copilot App** to move from "research to requirements to planning to implementation" while managing state in local files
- Select models based on the task (Opus 4.8 / Sonnet 4.6 / MAI-Code-1-Flash) and review costs

### Overall Flow
**Verify VS Code / Copilot App -> Learn the basics of token optimization -> Exercise: Develop a token-efficient task management tool (research -> requirements -> planning -> implementation -> cost review)**

We will use **GitHub Copilot App** throughout the workshop.

> aside positive
> Today's main exercise centers on **GitHub Copilot App**. Even in environments where issue-driven development using GitHub Issues / Pull Requests is unavailable, you can reproduce the same AI-driven development flow by treating **local files as "state"**, such as `research.md` / `spec.md` / `plan/`.

### Prerequisites
- GitHub Copilot Business license (876 Enterprise / GitHub EMU account)
- Windows or macOS
- Visual Studio Code (Agents Window) or GitHub Copilot App
- Ability to use GitHub Copilot CLI in your project working folder

> aside positive
> We assume that you have completed 876 Enterprise user account authentication and app setup according to the distributed "Event Preparation Guide." Please let us know if you have not completed these steps.

## Verify VS Code / Copilot App
Duration: 5

Today's main exercise centers on **GitHub Copilot App**. Starting from Copilot App, let's open the target folder and verify that everything works through VS Code and Terminal (Copilot CLI).

### 1. Verify Copilot App Launch

Launch Copilot App. If menus such as model selection, session management, and Autopilot appear, the app has launched successfully.

### 2. Open the Target Folder

Click the session **"+"**, then select and open your project working folder from **Local folder or repository**.

### 3. Verify a Response in the Session

Open a session with the **"+" button** to the right of the folder you opened, then enter the following in the input field and verify that you receive a response.

```
hoge
```

If you receive any response, Copilot App is working correctly.

### 4. Verify Access to VS Code

Launch VS Code from the **upper-right corner of the Copilot App screen**, then verify that you can access GitHub Copilot (that Copilot is enabled).

### 5. Verify Copilot CLI Launch

Launch Terminal from the **upper-right corner of the Copilot App screen**, then enter the following to verify that Copilot CLI starts.

```bash
copilot
```

If the interactive interface appears, it has started successfully. You can also use `/user` to verify the account currently signed in (and confirm that it is an 876 Enterprise user).

> aside negative
> If any component does not launch, verify that you are signed in with your GitHub EMU account (876 Enterprise). In the CLI, you can reauthenticate with `/login` or switch accounts with `/logout`.

## Reference: Tips for Reducing Token Usage / AI Credits
Duration: 10

Copilot Business uses AI Credits (UBB: usage-based billing). Before starting the next exercise, review these key points for **improving quality while reducing consumption**. The following is a summary of GitHub's "Agent Quality and Token Optimization" webinar.

### 1. Choose a Model That Is "Sufficient for the Task"
- Tasks requiring advanced reasoning, such as planning, design, and debugging: Opus / GPT-5.5 family
- Standard implementation: Sonnet / GPT-5.4 family
- Small refactors, repetitive tasks, and documentation updates: Haiku / mini family
- When in doubt, use **Auto Mode** as your default

### 2. Do Not Overload the Context
- Do not fill the context just because space is available. Models emphasize the beginning and end, while **the middle is more easily overlooked** (Context Rot)
- Use `/clear` for new tasks, and use `/compact` carefully for long sessions
- Provide only the necessary context and leave out unnecessary information

### 3. Remove Ambiguity from Prompts
- Give specific instructions and include the background and rationale
- State **stop conditions**, such as "stop if X occurs"
- Separate work into research, planning, and implementation (the next exercise follows exactly this pattern)

### 4. Add Mechanisms That Reduce Failures
- Agent failures compound in later steps. Add deterministic guardrails such as tests, linters, and scans
- Record recurring mistakes in a concise `copilot-instructions.md`

### Reference Links
- [Copilot models and billing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
- [Model comparison (Artificial Analysis)](https://artificialanalysis.ai/models?intelligence-index-cost=intelligence-index-cost)
- [What is Context Rot?](https://www.producttalk.org/context-rot/)
- [Token optimization tips by scenario](https://ashy-dune-0b4215a0f.7.azurestaticapps.net/detailed/index.html#/scenarios)
- [Token optimization webinar (recording)](https://github.ondemand.goldcast.io/on-demand/04d8b78c-7149-48df-91a1-68029e126c4a?utm_medium=email&utm_source=ent&utm_campaign=701Kg000000Pj6vIAC)
- [Example tool for reducing shell output: rtk](https://github.com/rtk-ai/rtk)
- [Copilot CodeAct Plugin for combining multiple tool calls](https://github.com/jsturtevant/copilot-codeact-plugin)

> aside positive
> For recommendations based on your actual usage, run `/chronicle cost-tips` in Copilot App / CLI (we will use it in the final exercise). In short: "**choose the right model x avoid unnecessary context x divide the work**." In the next exercise, you will experience this in a real development flow.

## Exercise: Develop a Token-Efficient Task Management Tool
Duration: 3

This is where today's exercise begins. Using **GitHub Copilot App**, you will build a small CLI task management tool in the order "research -> requirements -> planning -> implementation" while **optimizing token usage**.

### Why "Manage State Locally"?

Issue-driven development based on GitHub Issues / Pull Requests is powerful, but it may be **unavailable** due to internal policies or repository permissions. In this exercise, you will instead save each phase's deliverables as **local files**, as shown below, and treat those files themselves as development "state."

```
your-project/
├── research.md      ← Phase 1: Research results
├── spec.md          ← Phase 2: Implementation requirements
└── plan/
    ├── task.md      ← Phase 3: Major task
    ├── 1.md         ← Small task (implementation order)
    ├── 2.md
    └── 3.md
```

> aside positive
> The key is **one phase = one session**. When a phase ends, save its deliverables to files, then reset the context with `/clear` (or open a new session) before moving on. This keeps the context clean, reduces token consumption, and makes each phase's responsibility clear.

### What You'll Build

You will build a **simple CLI task management tool** with almost no dependencies. It is a small application that can add, list, complete, and delete tasks, with data stored in a local JSON file. By keeping the project small, you can focus on **how you build rather than what you build**.

## Phase 1: Research (research.md)
Duration: 8

Perform the initial research phase with **Copilot CLI**. Open Terminal from the **upper-right corner of the Copilot App screen**, then launch the CLI with `copilot`.

```bash
copilot
```

After it starts, use `/model` to select **Claude Opus 4.8**. This phase uses its advanced reasoning capabilities to establish a foundation for research and design.

```
/model
```

Next, request research with the `/research` command. `/research` is a dedicated command that investigates sources across the web and codebase and summarizes its findings.

```
/research I want to build a CLI task management tool with minimal dependencies. Compare the advantages and disadvantages of implementing it using only the standard libraries of Python and Node.js, including how each handles file storage (JSON) and parses CLI arguments. Do not implement it yet.
```

When the research results are returned, **review them in VS Code**. If you are satisfied with the content, ask the CLI to save it.

```
Save the current research results to research.md.
```

After saving, this phase is complete. Clear the session to reset its state.

```
/clear
```

> aside positive
> Clearing the session here is important. By not carrying the context from the completed "research" role into the next phase, you can begin the requirements phase with a clean state.

## Phase 2: Requirements Definition (spec.md)
Duration: 8

Open a new session and use `research.md` to compile the implementation requirements. Request requirements creation, validation, and saving in **a single prompt**.

`/rubber-duck` is a dedicated validation command that identifies logical gaps, omissions, and design inconsistencies that the original author may not notice.

```text
Read @research.md and create the implementation requirements (spec) for the CLI task management tool. Clearly specify the target users, functional requirements (add, list, complete, and delete), data format, CLI command specifications, non-functional requirements, and out of scope items (what will not be implemented). Validate the requirements with /rubber-duck, incorporate the findings, and save the result to spec.md.
```

After saving, **open a new session** and proceed to the next phase.

> aside positive
> **rubber-duck tip**: Adding "review it rigorously" produces more in-depth feedback. It is also important to use your own judgment rather than accepting every suggestion without question.

## Phase 3: Planning (plan/ Directory)
Duration: 7

Open another new session and create an implementation plan based on the research and requirements. Request plan creation and `/rubber-duck` validation in **a single prompt**.

```text
Create an implementation plan for the CLI task management tool based on @research.md and @spec.md.

- Break the work down into major tasks and small tasks
- Determine the implementation order
- Clearly state the blockers (dependencies and prerequisites) for each task
- Clearly state the test success and failure conditions for each task

Save the deliverables in the plan/ directory. Save the major task in plan/task.md. Create one file for each small task, using an implementation-order index and a descriptive filename that indicates what the plan covers, such as plan/1.[descriptive-plan-name].md, plan/2.[descriptive-plan-name].md, plan/3.[descriptive-plan-name].md, and so on.

Finally, validate the plan you created with /rubber-duck.
```

After saving, **open a new session** and proceed to the next phase.

> aside negative
> The quality of the planning phase largely determines the success or failure of the implementation phase. Before moving on, always verify in VS Code that each small task clearly states its test "success conditions and failure conditions."

## Phase 4: Implementation (Autopilot + Subsessions)
Duration: 10

Now it is time to implement. Open a new session in Copilot App, switch the model to **Claude Sonnet 4.6**, and enable **Autopilot mode** (in Autopilot, file creation, editing, and command execution proceed autonomously without confirmation).

Request the complete implementation according to the plan as follows.

```text
Implement the CLI task management tool according to @plan/task.md and the small tasks under @plan/ (1.md, 2.md, ...).

Implement each small task in a sub-session using the MAI-Code-1-Flash model. Follow the implementation order and continue until all tasks are complete, verifying that each task meets its test success conditions.
```

> aside positive
> **If you want to try a local LLM**, specify a BYOK model through LiteLLM for the sub-session execution.

The key here is **separation of responsibilities**.

- **Parent session (Sonnet 4.6 / Autopilot)**: Oversees the overall plan and manages task progress
- **Subsessions (MAI-Code-1-Flash or BYOK model through LiteLLM)**: Implement individual small tasks quickly and at low cost

> aside positive
> By assigning the lightweight and fast MAI-Code-1-Flash (or your local BYOK model) to small tasks as the "implementation hands," while using the more capable Sonnet 4.6 as the "orchestrator," you can **balance speed, cost, and quality**. This is a practical example of selecting models based on their purpose.

While implementation is in progress, watch the files change in VS Code. Seeing each task in `plan/` completed one by one gives you a direct sense of the local "state" moving forward.

If you get stuck, try the following:

- Paste the error message as-is and say, "Fix this"
- Rerun only the unsuccessful small task with a different model
- Review the test conditions for the relevant task in `plan/`

### Verify Functionality

After all tasks are complete, launch the application and verify its behavior.

```text
Launch the implemented CLI task management tool and verify that adding, listing, completing, and deleting tasks all work correctly. Fix anything that does not work.
```

Try running the commands yourself in the terminal and verify that the data is saved to a local file and persists after restarting. This will give you a stronger sense of what it means to "manage state locally."

## Phase 5: Review Costs
Duration: 4

After reaching a stopping point in implementation, review **how many tokens this exercise consumed and how much it cost**. Copilot session history is recorded in `~/.copilot/data.db`, so let's ask Copilot itself to aggregate the data.

In the session you used for implementation, make the following request (replace `[your project]` with the name of your working folder).

```text
Refer to the session table in ~/.copilot/data.db, measure the number of tokens used across all sessions for [your project], and calculate the cost according to the pricing table.
https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
```

The token count and estimated cost for each model will be displayed. Review how dividing the work into sessions by phase affected context consumption.

### Next Step: /chronicle cost-tips

Finally, run `/chronicle cost-tips` to review a collection of cost optimization tips.

```text
/chronicle cost-tips
```

Compare the displayed tips with this exercise's aggregated results and your practice of separating sessions by phase to identify exactly where you saved tokens.

> aside positive
> **What You Learned in This Exercise**: By **separating "research -> requirements -> planning -> implementation" into phase-specific sessions and saving deliverables to local files**, you can manage state and proceed with AI-driven development even in environments where issue-driven development is unavailable. Model selection (Opus 4.8 for design, Sonnet 4.6 for orchestration, and MAI-Code-1-Flash / BYOK for implementation) and validation with rubber-duck help balance quality and cost.

## Congratulations 🎉
Duration: 5

Thank you for your hard work during this one-hour workshop. Today, you experienced the following:

1. Basic Copilot App / CLI operations and the principles of token optimization
2. Research with `/research` and saving the results to research.md
3. Requirements definition (spec.md) and planning (plan/) with `/rubber-duck` validation
4. Implementation using Autopilot + subsessions (MAI-Code-1-Flash / BYOK)
5. Token and cost review using `~/.copilot/data.db` and `/chronicle cost-tips`

Through these activities, you experienced a flow for **using local files as "state" in spec-driven development**, even in environments where issue-driven development is unavailable.

### Trial License Program
For participants who do not have an 876 Enterprise Copilot license, we offer a **limited-time GitHub Copilot Business trial (3,000 AI Credits)**. Licenses are automatically granted through a web form, and capacity will be expanded gradually on a first-come, first-served basis. Please complete today's exercise and respond to the follow-up survey at a later date.

### Resources
- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [GitHub Copilot Best Practices](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot)

Please ask us anything during the Q&A session (17:45-17:55). Thank you!
