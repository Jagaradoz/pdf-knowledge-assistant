import arxiv
import os
import ssl

# Bypass SSL verification for arXiv API calls (common issue on some environments)
ssl._create_default_https_context = ssl._create_unverified_context

# 1. Create a folder to hold your PDFs so they don't clutter your main directory
pdf_dir = "my_pdf_dataset"
os.makedirs(pdf_dir, exist_ok=True)

print(f"Starting download. PDFs will be saved to: ./{pdf_dir}")

# 2. Set up the arXiv client
client = arxiv.Client()

# 3. Create your search query
# You can change "machine learning" to anything (e.g., "quantum physics", "economics")
search = arxiv.Search(
    query="machine learning",
    max_results=100, # <--- Change this number to get more or fewer PDFs
    sort_by=arxiv.SortCriterion.SubmittedDate
)

# 4. Fetch the results and download the PDFs
results = client.results(search)

for count, paper in enumerate(results, start=1):
    try:
        # Create a clean filename using the paper's ID
        filename = f"{paper.get_short_id()}.pdf"
        filepath = os.path.join(pdf_dir, filename)
        
        # Download the actual PDF file
        print(f"[{count}/100] Downloading: {paper.title}...")
        paper.download_pdf(dirpath=pdf_dir, filename=filename)
        
    except Exception as e:
        print(f"Failed to download {paper.title}. Error: {e}")

print("\nDownload complete! You now have a massive dataset for your RAG project.")
