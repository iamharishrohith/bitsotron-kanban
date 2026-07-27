import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# List of working dates (13/7/26 -> 29/7/26, except Sundays)
working_days = [
    ("2026-07-13", "Monday"),
    ("2026-07-14", "Tuesday"),
    ("2026-07-15", "Wednesday"),
    ("2026-07-16", "Thursday"),
    ("2026-07-17", "Friday"),
    ("2026-07-18", "Saturday"),
    # 19/07 Sunday excluded
    ("2026-07-20", "Monday"),
    ("2026-07-21", "Tuesday"),
    ("2026-07-22", "Wednesday"),
    ("2026-07-23", "Thursday"),
    ("2026-07-24", "Friday"),
    ("2026-07-25", "Saturday"),
    # 26/07 Sunday excluded
    ("2026-07-27", "Monday"),
    ("2026-07-28", "Tuesday"),
    ("2026-07-29", "Wednesday"),
]

# Team Member Details
team = {
    "tl": {"name": "Harish", "role": "Team Lead"},
    "sde1": {"name": "Keerthika", "role": "SDE-1 (Frontend)"},
    "sde2": {"name": "Akilan", "role": "SDE-2 (Frontend)"},
    "sde3": {"name": "Subhaharini", "role": "SDE-3 (Product & Planning)"}
}

# Task mapping per member per working day index (0 to 14)
tasks_data = {
    "tl": [
        # Kanban Board Building (July 13 - 15)
        {"title": "Internship Schedule Planning", "desc": "Planned the 3-week internship schedule and discussed the Kanban board app requirements with the team."},
        {"title": "PostgreSQL Schema Design", "desc": "Created the initial database tables design for tasks, daily updates, and activity logging."},
        {"title": "DB Setup Script Creation", "desc": "Wrote local SQL scripts to initialize tables and relationships for the Kanban database schema."},
        
        # Bitsotron Static Website (July 16 - 21)
        {"title": "Bitsotron Website Kickoff", "desc": "Conducted a team meeting to allocate website pages (Homepage, About Us, Services, FAQ)."},
        {"title": "Review UI Design Reference", "desc": "Reviewed the landing page layout wireframes and selected HSL Tailored color guidelines."},
        {"title": "Static Page Layout Validation", "desc": "Tested website sections for mobile view compatibility and discussed UI layout improvements."},
        {"title": "Next Sprint Planning Sync", "desc": "Met with team members to discuss homepage styling progress, review blockers, and schedule next tasks."},
        {"title": "Mock Presentation Planning", "desc": "Organized team presentation order and outlined design feedback parameters for our team reviews."},
        {"title": "Presentation Outlining", "desc": "Aligned MSME Hackathon rules and guidelines with the product presentation strategy for the deck slides."},
        
        # Hackathon PPT & Client discussion (July 22 - 25)
        {"title": "PPT Slide Outline Review", "desc": "Collaborated with Subhaharini on slide deck layouts, specifically reviewing business model and target user slides."},
        {"title": "Business Viability Outline", "desc": "Drafted content points for product pricing, target market, and financial feasibility slide updates."},
        {"title": "Mock Presentation Dry-Run", "desc": "Hosted a dry-run presentation, reviewed pitch timings, and suggested slide improvement points."},
        {"title": "Lead Client Demo Meeting", "desc": "Presented the live static website and PPT deck to the client, taking notes of all suggestions."},
        
        # Final Report and handover (July 27 - 29)
        {"title": "Consolidate Report Outline", "desc": "Coordinated final report structures and collected individual weekly internship summaries from team members."},
        {"title": "Review Team Report Drafts", "desc": "Reviewing SDE work summaries and compiled report drafts to check formatting consistency. (Continued)"},
        {"title": "Final Sign-off & Submission", "desc": "Perform final proofread of compiled internship files, verify database updates, and sign off on completion."}
    ],
    "sde1": [
        # Kanban Board Building (July 13 - 15)
        {"title": "Kanban Layout Research", "desc": "Studied Kanban board grid designs and sketched initial card and column structures on paper."},
        {"title": "Coded Board HTML Skeleton", "desc": "Wrote basic HTML elements for Kanban board headers, column sections, and navigation bars. (Continued)"},
        {"title": "Styled Card UI Elements", "desc": "Completed CSS styles for board task cards, user initials circles, and status badge designs. (Continued from July 14)"},
        
        # Bitsotron Static Website (July 16 - 21)
        {"title": "Wireframing Homepage Grid", "desc": "Created basic Figma layout sketch of the landing page, Hero section, and features structure."},
        {"title": "Homepage HTML Setup", "desc": "Coded structural HTML wrappers for Navbar, Hero section headers, and text boxes. (Continued)"},
        {"title": "Coding Hero & Services sections", "desc": "Implemented initial CSS styling for the page layout, aligning features and text spacing. (Continued from July 17)"},
        {"title": "About Us Page Skeleton", "desc": "Developed the layout structure and team profile grid section for the About Us page."},
        {"title": "Dynamic Grid Layout Review", "desc": "Tested About Us layout on browser and updated styling styles for text alignment and margins."},
        {"title": "Feedback Page Form Layout", "desc": "Created FAQ accordions layout and feedback form fields in static HTML page views."},
        
        # Hackathon PPT & Client discussion (July 22 - 25)
        {"title": "Website Styling Refinement", "desc": "Made styling updates and changed margin padding on landing pages based on previous team reviews. (Continued)"},
        {"title": "Design PPT Visual Assets", "desc": "Designed custom diagrams, icons, and schema graphics for the MSME pitch deck presentation."},
        {"title": "Static Web Image Optimizing", "desc": "Minified custom SVGs, converted raw images to WebP, and removed unused CSS style lines."},
        {"title": "Implement Client Feedback Tweaks", "desc": "Adjusted color palettes and alignment of page buttons based on notes from client demo meeting."},
        
        # Final Report and handover (July 27 - 29)
        {"title": "Draft Developer Documentation", "desc": "Writing developer hand-off guides, local setup instructions, and code folder hierarchy details. (Continued)"},
        {"title": "Compile Personal SDE Logs", "desc": "Gathering individual work milestones, code lines summary, and creating personal report files."},
        {"title": "Archiving Design Assets", "desc": "Remove temporary local assets, zip source Figma files, and verify code comments are clean."}
    ],
    "sde2": [
        # Kanban Board Building (July 13 - 15)
        {"title": "Repository & Next.js Setup", "desc": "Initialized local git repository and configured folder structure templates for the Next.js app."},
        {"title": "Neon DB Connection Setup", "desc": "Created Postgres connection scripts (db.js) and configured database parameters. (Continued)"},
        {"title": "Coded Get Tasks API Route", "desc": "Wrote backend API controllers (`/api/tasks`) in Next.js to retrieve and display database rows."},
        
        # Bitsotron Static Website (July 16 - 21)
        {"title": "Global CSS Design Config", "desc": "Defined CSS theme tokens for HSL Tailored color system, typography scale, and button shapes."},
        {"title": "Responsive Layout Shells", "desc": "Wrote layout CSS styles and responsive grids to align sections on desktop and tablet. (Continued)"},
        {"title": "Homepage Mobile Menu JS", "desc": "Programmed hamburger menu button triggers using vanilla JS overlay toggle events. (Continued from July 17)"},
        {"title": "Scroll Trigger Transitions", "desc": "Added Intersection Observer script triggers to run fade-in animation transitions during page scroll."},
        {"title": "Responsive Font Adjustments", "desc": "Fixed spacing overflow bugs on smaller screens using CSS clamp functions and viewport units."},
        {"title": "Contact Form Validation JS", "desc": "Wrote frontend JavaScript checks for the contact form email syntax and empty input errors."},
        
        # Hackathon PPT & Client discussion (July 22 - 25)
        {"title": "Contact Form Validation Tuning", "desc": "Refined form validation errors styling and tested animations for inline warning popups. (Continued)"},
        {"title": "Layout Adjustments For Slide Views", "desc": "Wrote slide display CSS templates to preview presentation flows directly in-app."},
        {"title": "Fix Next.js Build Warnings", "desc": "Ran project build checks, cleared ESLint warning logs, and resolved CSS import errors."},
        {"title": "Animate Live UI Hovers", "desc": "Added transition curves for live site cards and navbar hover states per client feedback notes."},
        
        # Final Report and handover (July 27 - 29)
        {"title": "Setup Vercel Deployment Link", "desc": "Configuring live domain details, connecting GitHub triggers, and building the production package. (Continued)"},
        {"title": "Live Link Post-Deploy Test", "desc": "Perform end-to-end check of form submissions, check site loading speed, and test live database links."},
        {"title": "Transfer Git Repository Access", "desc": "Merge last development branch, push final commits to main, and invite TL to repository ownership."}
    ],
    "sde3": [
        # Kanban Board Building (July 13 - 15)
        {"title": "Workflow Status Outlining", "desc": "Drafted definitions for board columns (Backlog, To Do, In Progress, Review, Done) and task rules."},
        {"title": "Project Configurations Setup", "desc": "Defined user credential structures, roles metadata, and colors configuration. (Continued)"},
        {"title": "Login Flow Integration Check", "desc": "Assisted Akilan in verifying credentials match and testing basic login overlay views."},
        
        # Bitsotron Static Website (July 16 - 21)
        {"title": "Website Copywriting Planning", "desc": "Outlined homepage copywriting content details and prepared initial product description sheets. (Continued)"},
        {"title": "Compile Landing Page Copy text", "desc": "Wrote primary landing page marketing texts, headers, and description paragraphs. (Continued from July 16)"},
        {"title": "Draft Contact Page Mockups", "desc": "Helped Keerthika design Contact Us page layout sections and form fields structure. (Continued)"},
        {"title": "Spell Check & Website Copy Review", "desc": "Read through current website texts to check grammar consistency and heading alignment."},
        {"title": "MSME Hackathon PPT Research", "desc": "Researched competitor ideas and gathered problem statements for the MSME Hackathon 6.0 deck."},
        {"title": "PPT Deck Structure Outlining", "desc": "Created presentation outline slides: Problem statement, Proposed Solution, and tech stack."},
        
        # Hackathon PPT & Client discussion (July 22 - 25)
        {"title": "Coded Pitch Slides (1-5)", "desc": "Drafted PPT slides covering project description, technical specs, and team contribution info. (Continued)"},
        {"title": "Coded Pitch Slides (6-10)", "desc": "Created slides covering financial feasibility, business model, and project advantages. (Continued from July 22)"},
        {"title": "Refine Slides Post Dry-Run", "desc": "Updated presentation slides text content and diagrams based on TL mock review feedback."},
        {"title": "Compile Client Meeting Notes", "desc": "Recorded client recommendations during the demo meeting and formatted feedback checklist."},
        
        # Final Report and handover (July 27 - 29)
        {"title": "Draft Report Intro & Scope", "desc": "Drafting internship report introductory sections, objectives guidelines, and index details. (Continued)"},
        {"title": "Compile Full Internship Report", "desc": "Assembling team work summaries and formatting the compiled report draft for final reviews."},
        {"title": "Final Report Formatting Checks", "desc": "Perform spelling check, add layout pages index, and bundle report documents for TL submission."}
    ]
}

def get_status_by_date(date_str, member_id):
    # Today is July 27, 2026
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    today_obj = datetime.date(2026, 7, 27)
    if date_obj < today_obj:
        return "Done"
    elif date_obj == today_obj:
        if member_id == "sde2":
            return "Code Review"
        else:
            return "In Progress"
    else:
        return "To Do"

def generate_excel_report(output_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Internship Task Report"
    
    # Enable grid lines explicitly
    ws.views.sheetView[0].showGridLines = True
    
    # 1. Title Block styling
    ws.merge_cells("A1:G1")
    title_cell = ws["A1"]
    title_cell.value = "INTERNSHIP WORK REPORT (13/07/2026 - 29/07/2026)"
    title_cell.font = Font(name="Segoe UI", size=15, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("A2:G2")
    subtitle_cell = ws["A2"]
    subtitle_cell.value = "Project: Kanban Board Building, Bitsotron Static Website & MSME Hackathon PPT"
    subtitle_cell.font = Font(name="Segoe UI", size=11, italic=True, color="EAF2F8")
    subtitle_cell.fill = PatternFill(start_color="2C3E50", end_color="2C3E50", fill_type="solid")
    subtitle_cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Set row heights for title
    ws.row_dimensions[1].height = 40
    ws.row_dimensions[2].height = 25
    
    # 2. Table Headers
    headers = ["Date", "Day", "Member Name", "Role", "Task Title", "Task Description", "Status"]
    header_fill = PatternFill(start_color="2E4053", end_color="2E4053", fill_type="solid")
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    header_align = Alignment(horizontal="center", vertical="center")
    
    ws.row_dimensions[4].height = 28
    for col_idx, header_text in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col_idx)
        cell.value = header_text
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
    
    thin_border = Border(
        left=Side(style='thin', color='BDC3C7'),
        right=Side(style='thin', color='BDC3C7'),
        top=Side(style='thin', color='BDC3C7'),
        bottom=Side(style='thin', color='BDC3C7')
    )
    
    zebra_fill = PatternFill(start_color="F8F9F9", end_color="F8F9F9", fill_type="solid")
    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    
    done_fill = PatternFill(start_color="D5F5E3", end_color="D5F5E3", fill_type="solid") # light green
    progress_fill = PatternFill(start_color="FCF3CF", end_color="FCF3CF", fill_type="solid") # light yellow
    review_fill = PatternFill(start_color="E8DAEF", end_color="E8DAEF", fill_type="solid") # light purple (review)
    todo_fill = PatternFill(start_color="EAECEE", end_color="EAECEE", fill_type="solid") # light grey
    
    done_font = Font(name="Segoe UI", size=10, color="196F3D", bold=True)
    progress_font = Font(name="Segoe UI", size=10, color="B7950B", bold=True)
    review_font = Font(name="Segoe UI", size=10, color="6C3483", bold=True)
    todo_font = Font(name="Segoe UI", size=10, color="5D6D7E", bold=True)
    
    current_row = 5
    
    # 3. Populate data sorted by date
    for idx, (date_str, day_name) in enumerate(working_days):
        day_fill = zebra_fill if idx % 2 == 0 else white_fill
        
        for member_id in ["tl", "sde1", "sde2", "sde3"]:
            member_info = team[member_id]
            task_info = tasks_data[member_id][idx]
            status = get_status_by_date(date_str, member_id)
            
            # Write Date
            cell_date = ws.cell(row=current_row, column=1, value=date_str)
            cell_date.alignment = Alignment(horizontal="center", vertical="center")
            
            # Write Day
            cell_day = ws.cell(row=current_row, column=2, value=day_name)
            cell_day.alignment = Alignment(horizontal="center", vertical="center")
            
            # Write Name
            cell_name = ws.cell(row=current_row, column=3, value=member_info["name"])
            cell_name.alignment = Alignment(horizontal="center", vertical="center")
            
            # Write Role
            cell_role = ws.cell(row=current_row, column=4, value=member_info["role"])
            cell_role.alignment = Alignment(horizontal="center", vertical="center")
            
            # Write Task Title
            cell_title = ws.cell(row=current_row, column=5, value=task_info["title"])
            cell_title.font = Font(name="Segoe UI", size=10, bold=True)
            cell_title.alignment = Alignment(horizontal="left", vertical="center")
            
            # Write Description
            cell_desc = ws.cell(row=current_row, column=6, value=task_info["desc"])
            cell_desc.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            
            # Write Status
            cell_status = ws.cell(row=current_row, column=7, value=status)
            cell_status.alignment = Alignment(horizontal="center", vertical="center")
            if status == "Done":
                cell_status.fill = done_fill
                cell_status.font = done_font
            elif status == "In Progress":
                cell_status.fill = progress_fill
                cell_status.font = progress_font
            elif status == "Code Review":
                cell_status.fill = review_fill
                cell_status.font = review_font
            else:
                cell_status.fill = todo_fill
                cell_status.font = todo_font
            
            # Apply row background (except status column which has its own fill)
            for c_idx in range(1, 7):
                ws.cell(row=current_row, column=c_idx).fill = day_fill
                
            # Apply borders and font to all cells in the row
            for c_idx in range(1, 8):
                c = ws.cell(row=current_row, column=c_idx)
                c.border = thin_border
                if c_idx != 5 and c_idx != 7: # Skip title and status which have custom font
                    c.font = Font(name="Segoe UI", size=10)
            
            # Calculate height based on description length
            desc_len = len(task_info["desc"])
            height = max(24, (desc_len // 50 + 1) * 16)
            ws.row_dimensions[current_row].height = height
            
            current_row += 1
            
    # Autofit columns
    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        if col_letter in ["A", "B", "C", "D", "G"]: # Centered code/short columns
            max_len = 0
            for cell in col:
                if cell.row > 2 and cell.value:
                    max_len = max(max_len, len(str(cell.value)))
            ws.column_dimensions[col_letter].width = max(max_len + 4, 12)
        elif col_letter == "E": # Title
            ws.column_dimensions[col_letter].width = 35
        elif col_letter == "F": # Description
            ws.column_dimensions[col_letter].width = 60
            
    # Save spreadsheet
    try:
        wb.save(output_path)
        print(f"Excel report successfully generated at: {output_path}")
    except PermissionError:
        dir_name = os.path.dirname(output_path)
        base_name = os.path.basename(output_path)
        name, ext = os.path.splitext(base_name)
        fallback_name = f"{name}_v2{ext}"
        fallback_path = os.path.join(dir_name, fallback_name) if dir_name else fallback_name
        wb.save(fallback_path)
        print(f"Permission denied to write to {output_path} (likely open in Excel). Saved to fallback: {fallback_path}")

if __name__ == "__main__":
    import os
    os.makedirs("scripts", exist_ok=True)
    
    # Save to local workspace
    generate_excel_report("Internship_Report_Tasks.xlsx")
    
    # Save to artifacts folder if path exists
    artifacts_dir = r"C:\Users\ipsha\.gemini\antigravity\brain\96a52e9c-511d-4460-bb06-2d47909391c9"
    if os.path.exists(artifacts_dir):
        generate_excel_report(os.path.join(artifacts_dir, "Internship_Report_Tasks.xlsx"))
