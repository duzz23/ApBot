import spacy


def main():
    with open('test_1/test_test1.txt', 'r') as f:
        input_text = f.read()
        print(input_text)

    input_text = input_text.replace('/', ' ')

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)

    texts = []
    poses = []

    for token in doc:
        texts.append(token.text)
        poses.append(token.pos_)

    result_dict = {}

    for text, pos in zip(texts, poses):
        if (pos == 'NUM' or pos == 'PROPN'):
            value = int(result_dict.get(text) or 0)
            result_dict.update({text: value + 1})

    print(result_dict)

    html = """
<!DOCTYPE html>
<html>
<body>
%insert%
</body>
</html>
    """

    insert = ''
    for key in result_dict.keys():
        insert += f'<h2 style="text-align:right;">{key}: {result_dict[key]}</h2> \n'

    html = html.replace('%insert%', insert)

    with open("test_1/result.html", 'w+') as f:
        f.write(html)

if __name__ == '__main__':
    main()