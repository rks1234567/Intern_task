import argparse
from summarizer import ArticleSummarizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("filename",help="Path to article file")
    parser.add_argument("--length",choices=["short", "medium", "long"],default="short")
    parser.add_argument("--style",choices=["formal", "casual"],default="formal")

    args = parser.parse_args()

    try:
        with open(args.filename, "r") as f:
            article = f.read()

        if not article.strip():
            raise ValueError(
                "Article file is empty"
            )

        summarizer = ArticleSummarizer()

        summary = summarizer.summarize(
            article,
            args.length,
            args.style
        )

        print("\nSummary:\n")
        print(summary)

    except FileNotFoundError:
        print("File not found")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")
    


