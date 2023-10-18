import requests

# v terminalu pustte: pip install tqdm
from tqdm import tqdm

URL = "https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat?d="
NUMBER_OF_ANIMALS = 10_000
animals = []

for number in (pbar := tqdm(range(1, NUMBER_OF_ANIMALS + 1))):
    # print(f"{URL}{number}")
    r = requests.get(url=f"{URL}{number}")
    # print(r)

    lines = r.text.splitlines()
    for line in lines:

        line = line.strip()

        if not line.startswith("<h2>"):
            continue
        line = line.replace("<h2>", "")
        line = line.replace("</h2></div>", "")

        pbar.write(line)
        animals.append(line)

