author: Your Name
summary: GitHub Copilot Workshop
id: github-copilot-workshop
categories: AI, Development
environments: Web
status: Published
feedback link: https://example.com/feedback

# GitHub Copilot Workshop

## About This Workshop
Duration: 5

Welcome to the GitHub Copilot Workshop! In this workshop, you will learn how to use GitHub Copilot to explain and improve code.
GitHub Copilot Chat allows you to interact with AI through a chat experience. Let's learn how to use GitHub Copilot through this workshop!

![GitHub Copilot Logo](github-copilot-workshop/img/octocat_copilot.png)

### Today's Goals
- Understand the various features of GitHub Copilot
- Use Agent Mode to develop a new application from scratch

### Prerequisites
- Visual Studio Code is installed
- You have a GitHub Copilot license
- You have a GitHub account

## Project Setup
Duration: 15

In this workshop, we will use the following GitHub repository:

**Project URL**: https://github.com/moulongzhang/2026-Github-Copilot-Workshop-Python

### Step 1: Create a Repository from the Template

First, open the project URL above in your browser and create your own repository from the template:

1. Open the project URL (https://github.com/moulongzhang/2026-Github-Copilot-Workshop-Python) in your browser
2. Click the **Use this template** button in the upper right and select **Create a new repository**

![Click Use this template button](github-copilot-workshop/img/f30b349b9da9c209.png)

3. On the repository creation screen, enter a repository name and click the **Create repository** button

![Click Create repository button](github-copilot-workshop/img/9b42f25710076003.png)

> aside negative
> **⚠️ Important**: When creating the repository, make sure to select **"Public"** for the **Visibility** setting. Some Copilot features and GitHub Actions may not work correctly with private repositories.

Once the template creation is complete, a new repository will be created under your GitHub account.

### Step 2: Set Up the Development Environment

Use the repository you created to set up a development environment with GitHub Codespaces:

1. Go to your repository page (`https://github.com/[your-username]/2026-Github-Copilot-Workshop-Python`)
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**

![Codespaces Setup](github-copilot-workshop/img/github-codespaces.png)

## Let's Build a Pomodoro Timer
Duration: 30

So far, you have learned the basic ways to use GitHub Copilot in VS Code. Now let's actually develop an application.

In this hands-on session, we will develop a Pomodoro timer application. This application will have the ability to set work and break durations and manage a timer.

We aim to create an application with a UI like the one below.

![Pomodoro Timer UI](github-copilot-workshop/img/8e24c2d7e6a91e1b.png)

First, let's create a new Python file in VS Code. Since we want to create this as a web application, we'll use Flask. Let's name the main file "app.py".

### Project Overview

We will create a web timer application for the Pomodoro Technique.

### Required Features

- 25-minute work timer
- 5-minute break timer
- Start, stop, and reset the timer
- Progress display and statistics
- Browser notifications and sound alerts
- Responsive Web UI

> aside positive
> **What is a Pomodoro Timer?**: The Pomodoro Technique is a time management method devised by Francesco Cirillo in the 1980s. It involves working in sets of "25 minutes of work + 5 minutes of break" (= 1 Pomodoro), repeating this cycle to maintain focus and work efficiently. For more details, see [Wikipedia: Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique).

## Thinking Through the Pomodoro Timer Design
Duration: 10

Rather than jumping straight into implementation, let's first consult Copilot about the approach and design to follow. From here on, we will proceed entirely in Agent Mode.

### Switching to Agent Mode

Select "Agent" from the Copilot Chat mode selector. The agent understands user intent and can execute tasks more autonomously.

![Agent Mode Selection 2](github-copilot-workshop/img/bcc926772d6a58dd.png)

![Agent Mode Selection](github-copilot-workshop/img/428f81215165ebb9.png)

### Design Consultation

When creating a web application with a UI like this, a useful feature is the ability to upload images to Copilot Chat. This allows Copilot to understand the UI image of your application.

First, save the UI image from the previous page as `pomodoro.png` in the project root. Then click `Add Context` in the chat input area and select "Image from Clipboard" or "Files & Folders...". Then select the UI image.

![VS Code Copilot Chat Context Menu](github-copilot-workshop/img/32ba4d287403b2f9.png)

![VS Code Copilot Chat Context Menu](github-copilot-workshop/img/aadb91ba110fa522.png)

Once the image is uploaded, it will appear in Copilot Chat.

Now, try entering the following prompt.

```
I plan to create a Pomodoro timer web app for this project. The attached image is the UI mock for the app. Please propose an architecture recommendation for building this app using Flask and HTML/CSS/JavaScript.
```

Copilot will then suggest a recommended web application architecture.

If you see areas for improvement or points that haven't been considered in this architecture, go ahead and point them out. For example:

```
Considering ease of unit testing, please identify any improvements or additions needed in the current architecture.
```

Once the architecture design is finalized through this exchange, let's save the content to a file. This way, you can reference the same architecture content even when opening a new chat session.

```
The architecture has been finalized through our conversation so far. Based on our discussion, please create a file called architecture.md in the project root that summarizes the web application architecture proposal.
```

> aside positive
> When you reach a good stopping point in your Copilot Chat conversation, starting a new conversation allows you to give Copilot clearer instructions. To start a new conversation, click the "New Conversation" button at the top of the chat window. When doing so, it's helpful to save content you want to reference in future chats - like this architecture document - to a file, as we did here.

## Let's Identify What Needs to Be Done
Duration: 10

At this point, the UI mock and architecture design are finalized. Let's consider what specific features need to be implemented. We'll consult Copilot Chat about this as well. Be sure to attach pomodoro.png and architecture.md.

```
Please identify all the features that need to be implemented to create this Pomodoro timer application.
```

![Feature List Review](github-copilot-workshop/img/8e24c2d7e6a91e1b.png)

![Feature Identification Example](github-copilot-workshop/img/20a6ec3e5b2f7c50.png)

Refine this content through your conversation with Copilot. Once finalized, save this content to a file called features.md, just as we did with the architecture.

```
Thank you. That looks good, so please write the list of features to implement in a file called features.md.
```

Now, before we start implementing, a key tip for using Copilot effectively is to avoid trying to implement large features all at once. Instead, start with small features first. This improves the accuracy of the code Copilot suggests, allowing for smoother development.

Let's also consult Copilot about how to break down this application development into appropriate increments. Here, attach pomodoro.png, architecture.md, and features.md.

```
I want to implement this Pomodoro timer application incrementally. Based on the attached image, architecture, and feature list, please propose a step-by-step implementation plan with appropriate granularity.
```

When I tried this, Copilot proposed a plan consisting of 6 steps. If there's anything you'd like to change, go ahead and tell Copilot. Then, save this content to a file called plan.md so you can reference it later. Think about what prompt you should use to give this instruction.

## Let's Implement
Duration: 30

With all the preparation in place, it's time to start implementing. Follow the implementation plan proposed in the previous step and implement features incrementally.

### 1. Preparing the Branch

Before starting implementation, let's create a working branch.

#### Step 1: Reset Staged Changes

Restore all currently staged changes back to the working directory:

```bash
git restore .
```

#### Step 2: Create a New Branch

Create and switch to the feature/pomodoro branch:

```bash
git checkout -b feature/pomodoro
```

### 2. Preparing the Project Structure

First, let's create the directory structure for the project according to our architecture.

Start by modifying the current project folder structure to support the architecture described in `architecture.md`. Move files and update configuration files as needed.

Then, attach `pomodoro.png`, `architecture.md`, and `plan.md`, and give Copilot the following instruction:

```
Please implement Step 1 of plan.md. If any existing files in this project need to be moved to different directories, please do that as well. If there are any additional considerations, please ask me.
```

In my case, Copilot came back with questions that needed consideration, as shown below. In such cases, provide the necessary information.

![Example Question from Copilot](github-copilot-workshop/img/8254991301cd47cd.png)

After that, Copilot proceeds with the Step 1 implementation. Once implementation is complete, Copilot will autonomously build the project and check for errors. If errors occur, it will make additional fixes to resolve them. This autonomous behavior is a key characteristic of Agent Mode.

Once implementation is complete, verify the following:

1. **Directory structure**: Does it follow the recommended architecture?
2. **Base files**: Have the necessary base files (app.py, HTML templates, CSS files, etc.) been created?
3. **Functionality check**: Run a quick test to make sure there are no errors

Below is an example of my Step 1 implementation result. The state of your application at this stage will likely differ.

![Step 1 Implementation Result Example](github-copilot-workshop/img/99241f822533e37a.png)

## Let's Write Tests
Duration: 20

Before continuing with implementation, let's write unit tests for the features we've implemented so far. Writing unit tests ensures that changes in later steps don't break existing functionality.

If unit tests were already implemented in the previous step, you can skip this page.

### Implementing Tests

Try running the following prompt.

```
There are currently no unit tests for the existing implementation. Please implement unit tests.
```

Copilot's agent will then ask for permission to execute commands to install unit test dependencies. Like this, the agent always asks the user for confirmation before executing any command. Click "Continue" to allow it to run the necessary commands.

![Copilot Test Implementation Confirmation](github-copilot-workshop/img/c724e1c653e2c6b3.png)

Copilot will then execute the command in VS Code's terminal and install the required dependencies. Similarly, for all subsequent commands, the agent will always ask the user for confirmation before execution. If an error occurs from running a command, the agent will make additional fixes to resolve it.

## Configuration for the Next Tasks
Duration: 20

In the following steps, we will use Copilot features on GitHub.com and the Cloud Agent. Let's configure the necessary settings.

### 1. GitHub Advanced Security (GHAS) Configuration

Enabling the Code Scanning feature of GitHub Advanced Security allows you to automatically detect code vulnerabilities.

1. Click the **Settings** tab in your repository
2. Select **Security** → **Code security** from the left sidebar
3. Click **Set up** in the **Code scanning** section

![GHAS Code Scanning Setup](github-copilot-workshop/img/code-scanning-setup.png)

4. Select **Default** (recommended)

![GHAS Default Configuration](github-copilot-workshop/img/code-scanning-default.png)

5. Click **Enable CodeQL**

This will enable automatic code scanning on push and pull request creation.

### 2. Enabling Copilot Features

Let's enable the Copilot features available on GitHub.

1. Click your profile icon in the upper right of GitHub
2. Select **Copilot settings**

![Copilot Settings](github-copilot-workshop/img/copilot-settings.png)

Enable the following features:

- **Editor preview features** - Preview features for the editor
- **Copilot CLI** - Use Copilot in the terminal
- **Copilot code review** - Code review feature
- **Copilot Cloud Agent** - Autonomous coding agent

> aside negative
>
> **Plan Limitations**: Advanced features such as Copilot Code Review, Cloud Agent, and Copilot CLI are only available with GitHub Copilot Business/Enterprise plans. These features are not available on the Free plan.

### 3. Enable Issues and Actions in Your Repository

> **⚠️ This step is only for users whose Issues or Actions are disabled.** Skip this if they are already enabled.

Repositories created from templates may have Issues and Actions disabled by default. Since we'll use them in later steps, enable them if they're currently disabled.

#### Enabling Issues

1. Click the **Settings** tab in your repository
2. Check the **Features** section under **General**
3. Check the box for **Issues**

#### Enabling Actions

1. Click the **Actions** tab in your repository
2. Click "I understand my workflows, go ahead and enable them" to enable

### 4. Creating a Personal Access Token (PAT) (Optional)

Create a Personal Access Token so that the Cloud Agent can operate within GitHub Actions.

#### Step 1: Create a Fine-grained PAT

Visit the following URL to create a new Fine-grained PAT:

[https://github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new)

Configuration:
- **Token name**: Enter any name you like (e.g., `copilot-workshop`)
- **Resource owner**: Select your personal user account (not an organization)
- **Repository access**: Select **Public repositories** (select Public repositories even if adding to a private repository)
- **Permissions**: Enable **Copilot Requests**

![Creating a Fine-grained PAT](github-copilot-workshop/img/fine-graiend-pat.png)

After creation, make sure to copy the displayed PAT.

> **⚠️ Note**: The PAT is only displayed on the screen immediately after creation. It cannot be viewed again after navigating away, so be sure to copy it at this time.

#### Step 2: Set as a GitHub Actions Repository Secret

Set the created PAT as a repository secret:

1. Click the **Settings** tab in your repository
2. Select **Secrets and variables** → **Actions** from the left sidebar
3. Click **New repository secret**
4. Enter the following:
   - **Name**: `COPILOT_GITHUB_TOKEN`
   - **Value**: Paste the PAT you just created
5. Click **Add secret**

#### Step 3: Verify Workflow Permissions

Verify the Actions workflow permissions so the Cloud Agent can automatically create Pull Requests:

1. Click the **Settings** tab in your repository
2. Select **Actions** → **General** from the left sidebar
3. In the **Workflow permissions** section, verify that **Allow GitHub Actions to create and approve pull requests** is checked
4. If not checked, enable it and click **Save**

> aside positive
>
> **Tip**: This setting allows the Copilot Cloud Agent to use Copilot's capabilities within GitHub Actions workflows.

## Implement the Remaining Features (Optional)
Duration: 20

This section is **optional**. Proceed if you have already learned the basic Copilot features and want to try more advanced implementations.

From here, let's implement the remaining features step by step as a free-form exercise.

Here are some tips that should be helpful.

### When You Want to Give Instructions About the UI

If you want to give instructions about specific UI elements, you can upload a screenshot of the UI to Copilot so it can recognize those elements. When doing so, it helps to circle or draw arrows on the screenshot to clearly indicate which elements you're referring to.

Alternatively, you can upload two screenshots — one showing the current state and one showing the expected state — to have Copilot identify the differences and make the UI match the expected design as closely as possible.

### When You Find Yourself Giving the Same Instructions Repeatedly

If you frequently give the same types of instructions when writing prompts or specifying context, you can have Copilot remember those instructions. Specifically, create a file called `.github/copilot-instructions.md` in your project and write the instructions there. When this file exists, Copilot automatically reads it and references those instructions in subsequent chats.

Below is a sample of custom instructions.

```markdown
This project implements a Pomodoro timer using Flask.

The following are important files in the project. Please reference these files as needed when responding to user instructions.
 - `pomodoro.png`: The UI mock for the application.
 - `architecture.md`: The application's architecture document.
 - `features.md`: The list of features to implement.
 - `plan.md`: The step-by-step implementation plan.
```

You can also include project-specific commands such as build and test commands, and Copilot will automatically use them.

### When Implementation Gets Stuck or You Can't Resolve a Bug

In such cases, try the following approaches:

- Instruct Copilot to output debug information, then have it analyze the output.
- Try a different model.

## Commit and Push to Git
Duration: 10

Let's commit the code you've created to the Git repository and push it to a remote branch. Here are two methods.

### Method A: Using Terminal Commands

The traditional method of running Git commands directly in the terminal:

```
git add .
git commit -m "Add Pomodoro timer feature"
git push origin feature/pomodoro
```

### Method B: Creating a Commit with Generative AI

Use Agent Mode to instruct Copilot directly to commit and push. Run the following prompt:

```
I've finished creating the feature. Please stage the code changes in git.

Then, please commit with an appropriate commit message and push the changes to the remote branch.
```

![MCP Git Workflow](github-copilot-workshop/img/mcp-git-workflow.png)

#### [Optional] Auto-creating GitHub Issues via MCP Server

Next, you can also use MCP Server to manage your implementation plan as GitHub Issues.

> aside negative
>
> **Note**: If the GitHub MCP server is not enabled, start the MCP server from the `.vscode/mcp.json` file:
>
> ```json
> {
>   "servers": {
>     "github-mcp-server": {
>       "type": "http",
>       "url": "https://api.githubcopilot.com/mcp/"
>     }
>   }
> }
> ```

```
Please create GitHub issues for each step in plan.md.
```

This instruction causes Copilot to:

1. Read the contents of `plan.md`
2. Create individual Issues for each step
3. Each Issue will include:
   - Step title and detailed description
   - Feature requirements to implement
   - Acceptance criteria
   - Appropriate labels and priority

This enables planned project management and agile development.

![MCP Issues](github-copilot-workshop/img/mcp-issues.png)

> aside positive
>
> **Benefits of MCP**: By using the GitHub MCP server, Copilot can directly access GitHub metadata such as repository information, Issues, Pull Requests, and branch information, enabling more detailed analysis and suggestions.

## [GitHub.com] Copilot Code Review
Duration: 15

After pushing, let's create a Pull Request on GitHub.com and leverage Copilot's code review features.

### Creating a Pull Request and Copilot Summary

1. Go to your repository on GitHub
2. Click **Open a pull request**
3. On the Pull Request creation screen, click **Copilot icon** >> **Summary**

![Copilot Summary in Pull Request](github-copilot-workshop/img/pull-request-copilot-summary.png)

Copilot will automatically generate a summary of the Pull Request.

### Assigning Copilot as a Reviewer

In the **Reviewers** section, assign **Copilot** to request a code review from Copilot.

> aside positive
>
> **Auto-assign Setting**: By going to Settings >> Branches >> Rulesets >> Require a pull request before merging >> Automatically request Copilot code review, Copilot will be automatically assigned when a Pull Request is opened.

![Copilot Auto-assign Settings](github-copilot-workshop/img/copilot-auto-assign-settings.png)

### Reviewing Copilot Code Review Results

After the Pull Request is opened, you can view the Copilot Code Review results:

- **Pull Request Overview**: Summary of code changes
- **Issues Found**: Identification of potential problems
- **Improvement Suggestions**: Specific suggestions for improving code quality

![Copilot Code Review Overview](github-copilot-workshop/img/copilot-code-review-overview.png)

### Static Vulnerability Scanning with GitHub Advanced Security

The Pull Request also displays results from GitHub Advanced Security (GHAS) static vulnerability scanning:

#### Reviewing Security Alerts

![GHAS Security Alerts](github-copilot-workshop/img/ghas-security-alerts.png)

- **High-severity Vulnerabilities**: Critical security issues
- **Copilot Autofix**: AI-powered automatic fix suggestions
- **Detailed Explanations**: Vulnerability details and remediation methods

#### Check Results Details

![GHAS Check Results](github-copilot-workshop/img/ghas-check-results.png)

> aside positive
>
> **Leveraging Copilot Autofix**: GitHub provides Copilot Autofix automatic fix suggestions for detected security vulnerabilities. This allows you to quickly resolve security issues.

## [GitHub.com] Copilot Cloud Agent
Duration: 20

Let's use the GitHub Copilot web interface to automatically generate improvement proposals as Issues and leverage the Cloud Agent.

### Auto-creating Issues with GitHub Copilot

1. Go to **GitHub.com** and click the **Copilot** icon in the upper right
2. Verify that your repository is added to the Chat context
3. Enter the following prompt:

```
Please create 3 issues for customizing the Pomodoro timer.

Pattern A: Enhanced Visual Feedback

Circular progress bar animation: Smooth decreasing animation based on remaining time
Color changes: Gradient transition from blue → yellow → red as time progresses
Background effects: Particle effects or ripple animations in the background during focus time
Test purpose: Measure the impact of visual immersion on user concentration

Pattern B: Improved Customizability

Flexible time settings: Choose from 15/25/35/45 minutes instead of a fixed 25 minutes
Theme switching: Dark/Light/Focus mode (minimal)
Sound settings: Toggle start/end/tick sounds on/off
Custom break duration: Choose from 5/10/15 minutes
Test purpose: Measure the impact of personalized settings on user retention

Pattern C: Gamification Elements

Experience point system: XP and level-ups based on completed Pomodoros
Achievement badges: Accomplishment system for "3 consecutive days", "10 completions this week", etc.
Weekly/monthly statistics: More detailed graph displays (completion rate, average focus time, etc.)
Streak display: Consecutive day count display
Test purpose: Measure the impact of gamification elements on motivation and continued usage
```

![Creating Issues with GitHub Copilot](github-copilot-workshop/img/github-copilot-issue-creation.png)

### Creating Issues and Assigning the Cloud Agent

1. **Copilot will automatically generate 3 Issues**
2. Review the content of each Issue and edit as needed
3. Click the **Create** button to create each Issue
4. After navigating to the Issue page, select **Copilot** in the **Assignees** section to assign the Cloud Agent

![Assigning Cloud Agent to Issue](github-copilot-workshop/img/coding-agent-assignment.png)

### Expected Pull Request Results

Once the Cloud Agent is assigned, you can expect the following results:

- **Automatic code implementation**: Feature implementation based on each Issue's requirements
- **Pull Request creation**: Automatic PR creation after implementation is complete
- **Comprehensive tests**: Including both unit tests and UI tests

#### Pattern A: Enhanced Visual Feedback

![Visual Feedback Enhancement PR Result](github-copilot-workshop/img/pr-result-visual-feedback.png)

#### Pattern B: Improved Customizability

![Customizability Improvement PR Result](github-copilot-workshop/img/pr-result-customization.png)

#### Pattern C: Gamification Elements

![Gamification Elements PR Result](github-copilot-workshop/img/pr-result-gamification.png)

> aside positive
>
> **Leveraging MCP Server**: The GitHub MCP Server and Playwright MCP Server are included in the Cloud Agent's initial setup. This enables not only unit tests but also automated UI verification through screenshots. The Cloud Agent visually verifies that implemented features work as expected, delivering higher quality code.

## [GitHub.com] Agentic Workflow
Duration: 15

By combining GitHub Actions with Copilot, let's experience an **Agentic Workflow** that detects code changes and automatically updates documentation.

### What is an Agentic Workflow?

An Agentic Workflow is a mechanism that leverages Copilot (AI) within GitHub Actions workflows to autonomously execute tasks in response to code changes. In this workshop, a workflow has been pre-configured to automatically update related documentation when changes are made to the Pomodoro timer code.

### 1. Merge the Pull Request into the Main Branch

Merge the Pull Request created in the previous step into the main branch.

1. Go to your repository on GitHub
2. Click the **Pull requests** tab
3. Open the target Pull Request
4. Click the **Merge pull request** button to merge

![Merging the Pull Request](github-copilot-workshop/img/merge-pull-request.png)

### 2. Verify the Workflow Execution

The Agentic Workflow was automatically triggered when you pushed the code.

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Verify that the **Pomodoro Documentation Sync** workflow is running

![Agentic Workflow Execution](github-copilot-workshop/img/agentic-workflow1.png)

This workflow automatically updates the documentation managed under `pomodoro/docs/` based on the changes whenever there are diffs in the code under `pomodoro/`.

### 3. Review the Pull Request

Once the Actions run completes, a **Pull Request** to update the documentation is automatically created.

1. Click the **Pull requests** tab
2. Review the PR created by Copilot
3. Review the documentation changes

### 4. Create Your Own Agentic Workflow

Now that you've seen the Agentic Workflow in action, let's create your own.

Run the following prompt in Agent Mode:

```
Please create a GitHub Agentic Workflow by referencing the following URL.
https://github.com/github/gh-aw/blob/main/create.md

The purpose of the workflow is as follows:
- It runs when code under copilotWebRelay is updated
- It updates the documentation under copilotWebRelay/docs based on the code under copilotWebRelay, ensuring that source code and documentation are always in sync

Commit the workflow file you created and create a Pull Request.
```

> aside positive
>
> **Possibilities of Agentic Workflows**: Beyond documentation updates, you can build Agentic Workflows for various tasks such as automatic test generation, automated code reviews, and release note creation.

## Let's Build an AI Chat Tool with the Copilot SDK
Duration: 10

From here, you'll use the **Copilot SDK** to build **Copilot Web Relay**, a generative AI chat tool that runs in the browser, **with a single prompt from Copilot CLI**.

### What is the Copilot SDK?

The **Copilot SDK** is an SDK for programmatically controlling GitHub Copilot CLI. It communicates with Copilot CLI via JSON-RPC, allowing you to integrate capabilities such as creating AI sessions, sending and receiving messages, and receiving streaming responses into your applications.

**SDK Repository**: [https://github.com/github/copilot-sdk](https://github.com/github/copilot-sdk)

### What You'll Build

You'll build a web application that lets you chat with AI in real time from your browser:

- **Frontend**: A browser-based chat UI (React + TypeScript)
- **Backend**: A Node.js server that manages AI sessions using the Copilot SDK
- **Real-time communication**: Delivers streaming responses over WebSocket

### Key Copilot SDK APIs

| API | Description |
|---|---|
| `CopilotClient` | Client that manages the connection to the CLI server |
| `client.createSession()` | Creates a new conversation session |
| `session.send()` | Sends a message |
| `session.on("assistant.message_delta")` | Receives streaming response chunks |
| `session.on("assistant.message")` | Receives the final response |
| `session.on("session.idle")` | Detects when session processing is complete |
| `approveAll` | Automatically approves all tool execution permissions |
| `createChatTools()` | Generates the standard toolset for chat |
| `hooks.onPreToolUse` | Hook that runs before tool execution (used for input validation, transformation, and more) |
| `hooks.onPostToolUse` | Hook that runs after tool execution (used for logging, processing results, and more) |

### Basic SDK Usage

```javascript
import { CopilotClient, approveAll, createChatTools } from "@github/copilot-sdk";

const client = new CopilotClient();
await client.start();

const session = await client.createSession({
    model: "gpt-5",
    onPermissionRequest: approveAll,
    tools: createChatTools(),
    hooks: {
        onPreToolUse: (input, invocation) => {
            console.log(`Before tool execution: ${invocation.toolName}`, input);
        },
        onPostToolUse: (input, invocation) => {
            console.log(`After tool execution: ${invocation.toolName}`, input);
        },
    },
});

session.on("assistant.message_delta", (event) => {
    process.stdout.write(event.data.deltaContent);
});

await session.send({ prompt: "Hello!" });
```

> aside positive
>
> **Key Point of This Section**: Without preparing a design document or detailed specifications, you'll build a web application using the SDK all at once simply by giving Copilot CLI **a single prompt**. Experience the productivity of AI-driven development.

## Implement with Vibe Coding
Duration: 60

Now that you understand the Copilot SDK overview, it's time to implement a browser-based AI chat tool with **Vibe Coding**.

### Step 1: Launch Copilot CLI

Launch Copilot CLI in the VS Code terminal.

```bash
copilot
```

### Step 2: Allow All Permissions

```
/allow-all
```

`/allow-all` is a command that grants **all permissions at once for tool execution, file access, and external URL access** to Copilot CLI.

Normally, Copilot CLI prompts the user for permission each time it reads or writes files, executes commands, or communicates externally for security purposes. Running `/allow-all` skips these confirmation prompts, allowing Copilot to autonomously create and edit files, install packages, start servers, and more.

> aside negative
>
> **Note**: `/allow-all` is only effective for the current session. For security reasons, only use it with trusted projects. If you prefer to grant permissions individually, you can also use `/add-dir` to set directory-level access permissions.

### Step 3: Select a High-end Model

```
/model
```

From the list of models, select the most powerful model (for example, Claude Opus 4.6). A high-end model with strong reasoning capabilities is effective for building a web application with multiple components.

### Step 4: Switch to Autopilot Mode

Press **Shift+Tab** to switch Copilot CLI to **Autopilot mode**. In Autopilot mode, Copilot autonomously creates and edits files and executes commands without asking for confirmation, making it ideal for Vibe Coding large implementations all at once.

### Step 5: Implement Everything at Once with a Single Prompt

Enter the following prompt in Copilot CLI. The `/fleet` command runs multiple agents in parallel to build a browser-based AI chat tool using the SDK all at once:

```
/fleet Using the Copilot SDK, build an AI chat web application that runs in a browser in the copilotWebRelay/ directory.

SDK reference: https://github.com/github/copilot-sdk

Requirements:
- Backend: Node.js + Express + WebSocket server
  - Manage sessions with the Copilot SDK's CopilotClient
  - Use model "gpt-5" with createSession(), and use approveAll for onPermissionRequest
  - Stream responses to the client over WebSocket with session.on("assistant.message_delta")
  - Notify the client of completion with session.on("session.idle")
- Frontend: React + TypeScript + Vite
  - Modern chat UI (message input field, send button, and chat history display)
  - Connect to the server with WebSocket and display streaming responses in real time
  - Support Markdown rendering
- Development environment: Backend and frontend can be started simultaneously with npm scripts
- Verify that the application works
```

> aside positive
>
> **Single-Prompt Tip**: Structure the requirements as a bulleted list and clearly specify the technology stack, SDK APIs, and expected behavior so Copilot can build the application accurately.

### Hints If You Get Stuck

If errors occur during implementation, try the following:

- **Share the error message directly with Copilot**: Simply saying "Please fix this error" is often enough
- **Check changes with `/diff`**: Verify there are no unintended changes
- **Switch models with `/model`**: Try a different model and retry

> aside negative
>
> **Common Pitfalls**:
> - **Installing the Copilot SDK**: Make sure `npm install @github/copilot-sdk` runs successfully
> - **Authentication**: Make sure Copilot CLI is signed in (the `copilot` command works)
> - **Vite WebSocket proxy**: You need to specify `http://` instead of `ws://` for the `target`
> - **React StrictMode**: `useEffect` running twice can cause unstable WebSocket connections

## Copilot Code Review — Code Review with Multiple Models
Duration: 30

Once the Copilot Web Relay implementation is complete, use the **review-related Copilot CLI commands** to conduct code reviews with multiple AI models. The goal is to identify quality, security, and performance issues from the different perspectives of multiple models.

### Key Commands for Reviews

Copilot CLI provides several commands that you can use for code reviews.

| Command | Description |
|---|---|
| `/review` | Run the code review agent to analyze changes |
| `/model` | Select the AI model to use (Claude, GPT, Gemini, etc.) |
| `/undo` | Rewind the previous turn and revert file changes |

### Step 1: Commit & Push the Code

In Copilot CLI, enter the following prompt to commit and push the implementation:

```
Stage all of the implemented Copilot Web Relay code with git add, commit it with an appropriate commit message, push it to the feature/copilot-web-relay branch, and create a pull request to the main branch.
```

### Step 2: Review with Multiple Models & Comment on the Pull Request

Enter the following prompt in Copilot CLI to run reviews with multiple models and post the results as a PR comment all at once:

```
/review Please review the Pull Request with each of the opus4.6 and GPT5.4 models, summarize the results, and leave the results as a comment on the Pull Request
```

With this prompt alone, the following actions are performed automatically:

- Code review by **Claude Opus 4.6**
- Code review by **GPT-5.4**
- Integration and comparison of each model's review results
- Posting a review comment on the Pull Request

If there is a problem with the changes, you can use `/undo` to rewind the previous turn and revert the file changes.

> aside positive
>
> **Benefits of Multi-Model Reviews**:
> - **Claude**: Strong at detecting logical inconsistencies and edge cases
> - **GPT**: Skilled at identifying a wide range of best practices
>
> Issues identified by multiple models are highly reliable and should be fixed first.

> aside positive
>
> **When to Use CLI Reviews vs. Code Review on GitHub.com**:
> - **`/review` (CLI)**: Immediately reviews local changes. It can detect issues early during development
> - **Copilot Code Review**: Reviews pull request changes and leaves formal review comments. It is ideal for team review workflows
>
> Combining both helps ensure quality from the early stages of development.

## Understand & Improve the Code
Duration: 20

Let's have Copilot explain the code of the Copilot SDK chat tool implemented through Vibe Coding to deepen our understanding. Then we'll find issues and implement improvements.

### 1. Request an Explanation of the Entire Codebase

First, let's get an overview of the implemented code. Enter the following prompt in Agent Mode:

```
Please review the entire codebase of the AI chat application under copilotWebRelay/ and explain the architecture, the role of each file, and the main processing flows. Focus especially on how the Copilot SDK is used (CopilotClient, createSession, and streaming responses).
```

The Copilot agent will automatically scan files in the project and explain the code structure and processing flows.

> aside positive
>
> **Tip**: In Agent Mode, Copilot automatically references files within the project when answering, so you don't need to manually add files to the context.

### 2. Identify Issues

Next, let's have Copilot identify issues from a code quality and security perspective:

```
Looking at the application under copilotWebRelay/ as a whole, what issues or areas for improvement do you see? Please analyze from the perspectives of design patterns, code quality, maintainability, and security.
```

You can also drill down into specific components:

```
Are there any issues with the backend WebSocket server and Copilot SDK session management? Please suggest improvements to error handling and resource management.
```

```
Are there any issues with the frontend WebSocket connection management or the display of streaming responses? Please check whether it follows React best practices.
```

### 3. Implement the Improvements

Let's have Copilot actually fix the issues found:

```
Please implement all of the improvements you suggested.
```

Copilot will propose changes directly to the code. Review the changes and use the "Keep" or "Undo" buttons in the chat to decide whether to accept them.

### 4. Verify Functionality

After implementing improvements, verify that the application continues to work correctly:

```
Please verify that the application works correctly after implementing the improvements. Start the backend, build the frontend, and verify operation in the browser.
```

> aside positive
>
> **Important**: In Agent Mode, Copilot operates more autonomously, so be sure to carefully review the proposed changes before accepting them. The agent may also automatically detect and attempt to fix errors that occur after code changes.

## Congratulations 🎉
Duration: 5

### What You Learned Today

In this workshop, you learned the following:

1. **Basic usage of GitHub Copilot**
2. **Code explanation and improvement with Agent Mode**
3. **Spec-driven development — controlling AI while implementing**
4. **AI-driven development using powerful models and tools**
5. **Building AI-powered applications with the Copilot SDK**

### Next Steps

- Try using Copilot in your actual projects
- Take on more complex application development
- Keep up with Copilot's new features
- Deploy the Copilot Web Relay to your own environment

### Resources

- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [GitHub Copilot Best Practices](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot)

Great work!
