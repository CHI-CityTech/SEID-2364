import os


def collate(root="."):
    docs = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden directories (e.g. .git)
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if not f.startswith("."):
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                docs.append(rel)
    docs.sort()
    return docs


if __name__ == "__main__":
    results = collate()
    print(f"Total documents: {len(results)}\n")
    for doc in results:
        print(doc)
