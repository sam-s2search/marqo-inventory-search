# E-Commerce Inventory Tensor Search - Powered By Marqo!
Marqo lets you search text or images in your Streamlit app, using it's [tensor search framework](https://github.com/marqo-ai/marqo).

## Installation
1. Marqo requires docker. Install [docker](https://docs.docker.com/get-docker/)
2. Use docker to run Marqo:
```bash
docker run --name marqo --privileged -p 8882:8882 --add-host host.docker.internal:host-gateway marqoai/marqo:0.0.3
```
3. Install the app framework Streamlit:
```bash
pip install streamlit
```

4. Marqo is distributed via [PyPI](https://pypi.org/project/marqo/)
```bash
pip install marqo
```

5. To index the e-commerce in _data/data.json_ checkout the [Marqo documentation](https://marqo.pages.dev/)

6. Run app using ```streamlit run app.py```