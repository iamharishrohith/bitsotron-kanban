const { Pool } = require('pg');

const pool = new Pool({
    connectionString: process.env.DATABASE_URL || 'postgresql://neondb_owner:npg_YQxu8LlSZMf4@ep-small-shape-atrhlzeh-pooler.c-9.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require'
});

// List of working dates (13/7/26 -> 29/7/26, except Sundays)
const workingDays = [
    { date: "2026-07-13", day: "Monday" },
    { date: "2026-07-14", day: "Tuesday" },
    { date: "2026-07-15", day: "Wednesday" },
    { date: "2026-07-16", day: "Thursday" },
    { date: "2026-07-17", day: "Friday" },
    { date: "2026-07-18", day: "Saturday" },
    // 19/07 Sunday
    { date: "2026-07-20", day: "Monday" },
    { date: "2026-07-21", day: "Tuesday" },
    { date: "2026-07-22", day: "Wednesday" },
    { date: "2026-07-23", day: "Thursday" },
    { date: "2026-07-24", day: "Friday" },
    { date: "2026-07-25", day: "Saturday" },
    // 26/07 Sunday
    { date: "2026-07-27", day: "Monday" },
    { date: "2026-07-28", day: "Tuesday" },
    { date: "2026-07-29", day: "Wednesday" },
];

const team = {
    "tl": { name: "Harish", role: "Team Lead" },
    "sde1": { name: "Keerthika", role: "SDE-1 (Frontend)" },
    "sde2": { name: "Akilan", role: "SDE-2 (Frontend)" },
    "sde3": { name: "Subhaharini", role: "SDE-3 (Product & Planning)" }
};

const tasksData = {
    "tl": [
        // Kanban Board Building (July 13 - 15)
        { title: "Internship Schedule Planning", desc: "Planned the 3-week internship schedule and discussed the Kanban board app requirements with the team." },
        { title: "PostgreSQL Schema Design", desc: "Created the initial database tables design for tasks, daily updates, and activity logging." },
        { title: "DB Setup Script Creation", desc: "Wrote local SQL scripts to initialize tables and relationships for the Kanban database schema." },
        
        // Bitsotron Static Website (July 16 - 21)
        { title: "Bitsotron Website Kickoff", desc: "Conducted a team meeting to allocate website pages (Homepage, About Us, Services, FAQ)." },
        { title: "Review UI Design Reference", desc: "Reviewed the landing page layout wireframes and selected HSL Tailored color guidelines." },
        { title: "Static Page Layout Validation", desc: "Tested website sections for mobile view compatibility and discussed UI layout improvements." },
        { title: "Next Sprint Planning Sync", desc: "Met with team members to discuss homepage styling progress, review blockers, and schedule next tasks." },
        { title: "Mock Presentation Planning", desc: "Organized team presentation order and outlined design feedback parameters for our team reviews." },
        { title: "Presentation Outlining", desc: "Aligned MSME Hackathon rules and guidelines with the product presentation strategy for the deck slides." },
        
        // Hackathon PPT & Client discussion (July 22 - 25)
        { title: "PPT Slide Outline Review", desc: "Collaborated with Subhaharini on slide deck layouts, specifically reviewing business model and target user slides." },
        { title: "Business Viability Outline", desc: "Drafted content points for product pricing, target market, and financial feasibility slide updates." },
        { title: "Mock Presentation Dry-Run", desc: "Hosted a dry-run presentation, reviewed pitch timings, and suggested slide improvement points." },
        { title: "Lead Client Demo Meeting", desc: "Presented the live static website and PPT deck to the client, taking notes of all suggestions." },
        
        // Final Report and handover (July 27 - 29)
        { title: "Consolidate Report Outline", desc: "Coordinated final report structures and collected individual weekly internship summaries from team members." },
        { title: "Review Team Report Drafts", desc: "Reviewing SDE work summaries and compiled report drafts to check formatting consistency. (Continued)" },
        { title: "Final Sign-off & Submission", desc: "Perform final proofread of compiled internship files, verify database updates, and sign off on completion." }
    ],
    "sde1": [
        // Kanban Board Building (July 13 - 15)
        { title: "Kanban Layout Research", desc: "Studied Kanban board grid designs and sketched initial card and column structures on paper." },
        { title: "Coded Board HTML Skeleton", desc: "Wrote basic HTML elements for Kanban board headers, column sections, and navigation bars. (Continued)" },
        { title: "Styled Card UI Elements", desc: "Completed CSS styles for board task cards, user initials circles, and status badge designs. (Continued from July 14)" },
        
        // Bitsotron Static Website (July 16 - 21)
        { title: "Wireframing Homepage Grid", desc: "Created basic Figma layout sketch of the landing page, Hero section, and features structure." },
        { title: "Homepage HTML Setup", desc: "Coded structural HTML wrappers for Navbar, Hero section headers, and text boxes. (Continued)" },
        { title: "Coding Hero & Services sections", desc: "Implemented initial CSS styling for the page layout, aligning features and text spacing. (Continued from July 17)" },
        { title: "About Us Page Skeleton", desc: "Developed the layout structure and team profile grid section for the About Us page." },
        { title: "Dynamic Grid Layout Review", desc: "Tested About Us layout on browser and updated styling styles for text alignment and margins." },
        { title: "Feedback Page Form Layout", desc: "Created FAQ accordions layout and feedback form fields in static HTML page views." },
        
        // Hackathon PPT & Client discussion (July 22 - 25)
        { title: "Website Styling Refinement", desc: "Made styling updates and changed margin padding on landing pages based on previous team reviews. (Continued)" },
        { title: "Design PPT Visual Assets", desc: "Designed custom diagrams, icons, and schema graphics for the MSME pitch deck presentation." },
        { title: "Static Web Image Optimizing", desc: "Minified custom SVGs, converted raw images to WebP, and removed unused CSS style lines." },
        { title: "Implement Client Feedback Tweaks", desc: "Adjusted color palettes and alignment of page buttons based on notes from client demo meeting." },
        
        // Final Report and handover (July 27 - 29)
        { title: "Draft Developer Documentation", desc: "Writing developer hand-off guides, local setup instructions, and code folder hierarchy details. (Continued)" },
        { title: "Compile Personal SDE Logs", desc: "Gathering individual work milestones, code lines summary, and creating personal report files." },
        { title: "Archiving Design Assets", desc: "Remove temporary local assets, zip source Figma files, and verify code comments are clean." }
    ],
    "sde2": [
        // Kanban Board Building (July 13 - 15)
        { title: "Repository & Next.js Setup", desc: "Initialized local git repository and configured folder structure templates for the Next.js app." },
        { title: "Neon DB Connection Setup", desc: "Created Postgres connection scripts (db.js) and configured database parameters. (Continued)" },
        { title: "Coded Get Tasks API Route", desc: "Wrote backend API controllers (`/api/tasks`) in Next.js to retrieve and display database rows." },
        
        // Bitsotron Static Website (July 16 - 21)
        { title: "Global CSS Design Config", desc: "Defined CSS theme tokens for HSL Tailored color system, typography scale, and button shapes." },
        { title: "Responsive Layout Shells", desc: "Wrote layout CSS styles and responsive grids to align sections on desktop and tablet. (Continued)" },
        { title: "Homepage Mobile Menu JS", desc: "Programmed hamburger menu button triggers using vanilla JS overlay toggle events. (Continued from July 17)" },
        { title: "Scroll Trigger Transitions", desc: "Added Intersection Observer script triggers to run fade-in animation transitions during page scroll." },
        { title: "Responsive Font Adjustments", desc: "Fixed spacing overflow bugs on smaller screens using CSS clamp functions and viewport units." },
        { title: "Contact Form Validation JS", desc: "Wrote frontend JavaScript checks for the contact form email syntax and empty input errors." },
        
        // Hackathon PPT & Client discussion (July 22 - 25)
        { title: "Contact Form Validation Tuning", desc: "Refined form validation errors styling and tested animations for inline warning popups. (Continued)" },
        { title: "Layout Adjustments For Slide Views", desc: "Wrote slide display CSS templates to preview presentation flows directly in-app." },
        { title: "Fix Next.js Build Warnings", desc: "Ran project build checks, cleared ESLint warning logs, and resolved CSS import errors." },
        { title: "Animate Live UI Hovers", desc: "Added transition curves for live site cards and navbar hover states per client feedback notes." },
        
        // Final Report and handover (July 27 - 29)
        { title: "Setup Vercel Deployment Link", desc: "Configuring live domain details, connecting GitHub triggers, and building the production package. (Continued)" },
        { title: "Live Link Post-Deploy Test", desc: "Perform end-to-end check of form submissions, check site loading speed, and test live database links." },
        { title: "Transfer Git Repository Access", desc: "Merge last development branch, push final commits to main, and invite TL to repository ownership." }
    ],
    "sde3": [
        // Kanban Board Building (July 13 - 15)
        { title: "Workflow Status Outlining", desc: "Drafted definitions for board columns (Backlog, To Do, In Progress, Review, Done) and task rules." },
        { title: "Project Configurations Setup", desc: "Defined user credential structures, roles metadata, and colors configuration. (Continued)" },
        { title: "Login Flow Integration Check", desc: "Assisted Akilan in verifying credentials match and testing basic login overlay views." },
        
        // Bitsotron Static Website (July 16 - 21)
        { title: "Website Copywriting Planning", desc: "Outlined homepage copywriting content details and prepared initial product description sheets. (Continued)" },
        { title: "Compile Landing Page Copy text", desc: "Wrote primary landing page marketing texts, headers, and description paragraphs. (Continued from July 16)" },
        { title: "Draft Contact Page Mockups", desc: "Helped Keerthika design Contact Us page layout sections and form fields structure. (Continued)" },
        { title: "Spell Check & Website Copy Review", desc: "Read through current website texts to check grammar consistency and heading alignment." },
        { title: "MSME Hackathon PPT Research", desc: "Researched competitor ideas and gathered problem statements for the MSME Hackathon 6.0 deck." },
        { title: "PPT Deck Structure Outlining", desc: "Created presentation outline slides: Problem statement, Proposed Solution, and tech stack." },
        
        // Hackathon PPT & Client discussion (July 22 - 25)
        { title: "Coded Pitch Slides (1-5)", desc: "Drafted PPT slides covering project description, technical specs, and team contribution info. (Continued)" },
        { title: "Coded Pitch Slides (6-10)", desc: "Created slides covering financial feasibility, business model, and project advantages. (Continued from July 22)" },
        { title: "Refine Slides Post Dry-Run", desc: "Updated presentation slides text content and diagrams based on TL mock review feedback." },
        { title: "Compile Client Meeting Notes", desc: "Recorded client recommendations during the demo meeting and formatted feedback checklist." },
        
        // Final Report and handover (July 27 - 29)
        { title: "Draft Report Intro & Scope", desc: "Drafting internship report introductory sections, objectives guidelines, and index details. (Continued)" },
        { title: "Compile Full Internship Report", desc: "Assembling team work summaries and formatting the compiled report draft for final reviews." },
        { title: "Final Report Formatting Checks", desc: "Perform spelling check, add layout pages index, and bundle report documents for TL submission."}
    ]
};

function genId() {
    return Math.random().toString(16).substring(2, 6) + '-' + Math.random().toString(16).substring(2, 6);
}

function getStatusByDate(dateStr, memberId) {
    const d = new Date(dateStr);
    const today = new Date("2026-07-27");
    
    d.setHours(0,0,0,0);
    today.setHours(0,0,0,0);
    
    if (d < today) {
        return "done";
    } else if (d.getTime() === today.getTime()) {
        return (memberId === "sde2") ? "review" : "progress";
    } else {
        return "todo";
    }
}

async function run() {
    try {
        console.log("Connecting to Neon PostgreSQL...");
        
        // 1. Clear existing tasks and status logs
        console.log("Cleaning tasks and status_logs tables...");
        await pool.query("DELETE FROM tasks");
        await pool.query("DELETE FROM status_logs");
        
        console.log("Populating tasks...");
        
        for (let idx = 0; idx < workingDays.length; idx++) {
            const { date, day } = workingDays[idx];
            
            for (const memberId of ["tl", "sde1", "sde2", "sde3"]) {
                const member = team[memberId];
                const task = tasksData[memberId][idx];
                const taskId = genId();
                const status = getStatusByDate(date, memberId);
                
                const createdTime = new Date(`${date}T09:00:00Z`).getTime();
                const progressTime = new Date(`${date}T10:00:00Z`).getTime();
                const reviewTime = new Date(`${date}T16:00:00Z`).getTime();
                const doneTime = new Date(`${date}T17:00:00Z`).getTime();
                
                let activity = [
                    { text: `Task created by Harish (TL)`, time: createdTime }
                ];
                
                let currentTimestamp = createdTime;
                
                if (status === "progress") {
                    activity.push({
                        text: `${member.name} accepted the task (moved to In Progress)`,
                        time: progressTime
                    });
                    currentTimestamp = progressTime;
                } else if (status === "review") {
                    activity.push({
                        text: `${member.name} accepted the task (moved to In Progress)`,
                        time: progressTime
                    });
                    activity.push({
                        text: `${member.name} requested code review (moved to Code Review)`,
                        time: reviewTime
                    });
                    currentTimestamp = reviewTime;
                } else if (status === "done") {
                    activity.push({
                        text: `${member.name} accepted the task (moved to In Progress)`,
                        time: progressTime
                    });
                    activity.push({
                        text: `${member.name} completed the task (moved to Done)`,
                        time: doneTime
                    });
                    currentTimestamp = doneTime;
                }
                
                const priority = (idx % 3 === 0) ? "high" : "medium";
                
                // Insert Task
                await pool.query(
                    `INSERT INTO tasks (id, title, description, status, priority, due_date, assignees, activity, created_by, created_at, updated_at)
                     VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)`,
                    [
                        taskId,
                        task.title,
                        task.desc,
                        status,
                        priority,
                        date,
                        JSON.stringify([memberId]),
                        JSON.stringify(activity),
                        "tl",
                        createdTime,
                        currentTimestamp
                    ]
                );
                
                // Insert Status Logs for history tracking
                // 1. Creation log
                await pool.query(
                    `INSERT INTO status_logs (id, task_id, task_title, user_name, from_status, to_status, timestamp)
                     VALUES ($1, $2, $3, $4, $5, $6, $7)`,
                    [
                        genId(),
                        taskId,
                        task.title,
                        "Harish",
                        "None (Created)",
                        "Backlog",
                        createdTime
                    ]
                );
                
                // 2. To Do / Backlog to In Progress (for done, progress, and review statuses)
                if (status === "progress" || status === "review" || status === "done") {
                    await pool.query(
                        `INSERT INTO status_logs (id, task_id, task_title, user_name, from_status, to_status, timestamp)
                         VALUES ($1, $2, $3, $4, $5, $6, $7)`,
                        [
                            genId(),
                            taskId,
                            task.title,
                            member.name,
                            "Backlog",
                            "In Progress",
                            progressTime
                        ]
                    );
                }
                
                // 3. In Progress to Code Review (for review status)
                if (status === "review") {
                    await pool.query(
                        `INSERT INTO status_logs (id, task_id, task_title, user_name, from_status, to_status, timestamp)
                         VALUES ($1, $2, $3, $4, $5, $6, $7)`,
                        [
                            genId(),
                            taskId,
                            task.title,
                            member.name,
                            "In Progress",
                            "Code Review",
                            reviewTime
                        ]
                    );
                }
                
                // 4. In Progress to Done (for done status)
                if (status === "done") {
                    await pool.query(
                        `INSERT INTO status_logs (id, task_id, task_title, user_name, from_status, to_status, timestamp)
                         VALUES ($1, $2, $3, $4, $5, $6, $7)`,
                        [
                            genId(),
                            taskId,
                            task.title,
                            member.name,
                            "In Progress",
                            "Done",
                            doneTime
                        ]
                    );
                }
            }
        }
        
        console.log("Database successfully populated with 60 tasks!");
    } catch (err) {
        console.error("Error populating database:", err);
    } finally {
        await pool.end();
    }
}

run();
