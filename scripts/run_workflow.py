from normalize_links import normalize_links
from lower_case_filenames import lowercase_markdown_filenames
from update_inbound_references import update_inbound_references

if __name__ == '__main__':
    lowercase_markdown_filenames()
    normalize_links()
    update_inbound_references()
