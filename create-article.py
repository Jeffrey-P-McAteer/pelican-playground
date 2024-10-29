
import os
import sys
import datetime

def get_categories_in(folder):
    categories = set()
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path) and ( file_name.endswith('.md') or file_name.endswith('.MD') ):
            with open(file_path, 'r') as fd:
                line_i = -1
                while line := fd.readline():
                    line_i += 1
                    if line_i > 5:
                        break
                    if line.startswith('Category: '):
                        categories.add( line[9:].strip() )

    categories = sorted(list(categories))
    return categories


def main(args=sys.argv):
    content_dir = os.path.join(
        os.path.dirname(__file__), 'content', 'content'
    )
    article_name = ''
    while len(article_name.strip()) < 2:
        article_name = input('Name of article: ').strip()

    file_name = '-'.join( ''.join(c for c in token if c.isalnum()) for token in article_name.split())
    file_name = file_name.replace('--', '-').replace('--', '-')
    file_path = os.path.join(content_dir, file_name+'.md')
    if os.path.exists(file_path):
        print(f'Warning!')
        print(f'  {file_path}')
        print(f'Already exists!')
        yn = input('Delete the existing file? (y/N)')
        if not 'y' in yn.lower():
            print('Exiting...')
            return

    # First scan other articles for categories
    print('=== Categories ===')
    for c in get_categories_in(content_dir):
        print(f' - {c}')
    print()

    category = input('Article Category: ').strip()
    category_line = ''
    if len(category) > 1:
        category_line = f'Category: {category}'

    date_ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(file_path, 'w') as fd:
        fd.write(f'''
Title: {article_name}
Date: {date_ts}
{category_line}

'''.strip()+(4 * os.linesep))
    print(f'Go edit {file_path}')

if __name__ == '__main__':
    main()


