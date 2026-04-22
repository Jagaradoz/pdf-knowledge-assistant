import arxiv
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

MAX_RESULTS = 10
pdf_dir = "data/raw/"
os.makedirs(pdf_dir, exist_ok=True)

print(f"Starting download. PDFs will be saved to: ./{pdf_dir}")

client = arxiv.Client()
search = arxiv.Search(
    query="machine learning",
    max_results=MAX_RESULTS,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

results = client.results(search)

for count, paper in enumerate(results, start=1):
    try:
        filename = f"{paper.get_short_id()}.pdf"
        filepath = os.path.join(pdf_dir, filename)
        
        print(f"[{count}/{MAX_RESULTS}] Downloading: {paper.title}...")
        paper.download_pdf(dirpath=pdf_dir, filename=filename)
        
    except Exception as e:
        print(f"Failed to download {paper.title}. Error: {e}")

print("\nDownload complete!")
