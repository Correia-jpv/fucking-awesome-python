# Awesome Python

An opinionated list of Python frameworks, libraries, tools, and resources.

# **Sponsors**

> The **#10 most-starred repo on GitHub**. Put your product in front of Python developers. [Become a sponsor](SPONSORSHIP.md).

# Categories

**AI & ML**

- [AI and Agents](#ai-and-agents)
- [Deep Learning](#deep-learning)
- [Machine Learning](#machine-learning)
- [Natural Language Processing](#natural-language-processing)
- [Computer Vision](#computer-vision)
- [Recommender Systems](#recommender-systems)

**Web Development**

- [Web Frameworks](#web-frameworks)
- [Web APIs](#web-apis)
- [Web Servers](#web-servers)
- [WebSocket](#websocket)
- [Template Engines](#template-engines)
- [Web Asset Management](#web-asset-management)
- [Authentication](#authentication)
- [Admin Panels](#admin-panels)
- [CMS](#cms)
- [Static Site Generators](#static-site-generators)

**HTTP & Scraping**

- [HTTP Clients](#http-clients)
- [Web Scraping](#web-scraping)
- [Email](#email)

**Database & Storage**

- [ORM](#orm)
- [Database Drivers](#database-drivers)
- [Database](#database)
- [Caching](#caching)
- [Search](#search)
- [Serialization](#serialization)

**Data & Science**

- [Data Analysis](#data-analysis)
- [Data Validation](#data-validation)
- [Data Visualization](#data-visualization)
- [Geolocation](#geolocation)
- [Science](#science)
- [Quantum Computing](#quantum-computing)

**Developer Tools**

- [Algorithms and Design Patterns](#algorithms-and-design-patterns)
- [Interactive Interpreter](#interactive-interpreter)
- [Code Analysis](#code-analysis)
- [Testing](#testing)
- [Debugging Tools](#debugging-tools)
- [Build Tools](#build-tools)
- [Documentation](#documentation)

**DevOps**

- [DevOps Tools](#devops-tools)
- [Distributed Computing](#distributed-computing)
- [Task Queues](#task-queues)
- [Job Schedulers](#job-schedulers)
- [Logging](#logging)
- [Network Virtualization](#network-virtualization)

**CLI & GUI**

- [CLI Development](#cli-development)
- [CLI Tools](#cli-tools)
- [GUI Development](#gui-development)

**Text & Documents**

- [Text Processing](#text-processing)
- [HTML Manipulation](#html-manipulation)
- [File Format Processing](#file-format-processing)
- [File Manipulation](#file-manipulation)

**Media**

- [Image Processing](#image-processing)
- [Audio & Video Processing](#audio--video-processing)
- [Game Development](#game-development)

**Python Language**

- [Implementations](#implementations)
- [Built-in Classes Enhancement](#built-in-classes-enhancement)
- [Functional Programming](#functional-programming)
- [Asynchronous Programming](#asynchronous-programming)
- [Date and Time](#date-and-time)

**Python Toolchain**

- [Environment Management](#environment-management)
- [Package Management](#package-management)
- [Package Repositories](#package-repositories)
- [Distribution](#distribution)
- [Configuration Files](#configuration-files)

**Security**

- [Cryptography](#cryptography)
- [Penetration Testing](#penetration-testing)

**Miscellaneous**

- [Hardware](#hardware)
- [Microsoft Windows](#microsoft-windows)
- [Miscellaneous](#miscellaneous)

---

**AI & ML**

## AI and Agents

_Libraries for building AI applications, LLM integrations, and autonomous agents._

- Agent Skills
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1🍴</code></b> [django-ai-plugins](https://github.com/vintasoftware/django-ai-plugins)) - Django backend agent skills for Django, DRF, Celery, and Django-specific code review.
  - <b><code>&nbsp;&nbsp;&nbsp;490⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;17🍴</code></b> [sentry-skills](https://github.com/getsentry/skills)) - Python-focused engineering skills for code review, debugging, and backend workflows.
  - <b><code>&nbsp;&nbsp;4096⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;362🍴</code></b> [trailofbits-skills](https://github.com/trailofbits/skills)) - Python-friendly security skills for auditing, testing, and safer backend development.
- Orchestration
  - <b><code>&nbsp;56406⭐</code></b> <b><code>&nbsp;&nbsp;8480🍴</code></b> [autogen](https://github.com/microsoft/autogen)) - A programming framework for building agentic AI applications.
  - <b><code>&nbsp;47521⭐</code></b> <b><code>&nbsp;&nbsp;6439🍴</code></b> [crewai](https://github.com/crewAIInc/crewAI)) - A framework for orchestrating role-playing autonomous AI agents for collaborative task solving.
  - <b><code>&nbsp;33260⭐</code></b> <b><code>&nbsp;&nbsp;2739🍴</code></b> [dspy](https://github.com/stanfordnlp/dspy)) - A framework for programming, not prompting, language models.
  - <b><code>131525⭐</code></b> <b><code>&nbsp;21679🍴</code></b> [langchain](https://github.com/langchain-ai/langchain)) - Building applications with LLMs through composability.
  - <b><code>&nbsp;15935⭐</code></b> <b><code>&nbsp;&nbsp;1840🍴</code></b> [pydantic-ai](https://github.com/pydantic/pydantic-ai)) - A Python agent framework for building generative AI applications with structured schemas.
- Data Layer
  - <b><code>&nbsp;12626⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;984🍴</code></b> [instructor](https://github.com/567-labs/instructor)) - A library for extracting structured data from LLMs, powered by Pydantic.
  - <b><code>&nbsp;48120⭐</code></b> <b><code>&nbsp;&nbsp;7117🍴</code></b> [llama-index](https://github.com/run-llama/llama_index)) - A data framework for your LLM application.
  - <b><code>&nbsp;51404⭐</code></b> <b><code>&nbsp;&nbsp;5751🍴</code></b> [mem0](https://github.com/mem0ai/mem0)) - An intelligent memory layer for AI agents enabling personalized interactions.
- Pre-trained Models and Inference
  - <b><code>&nbsp;33201⭐</code></b> <b><code>&nbsp;&nbsp;6880🍴</code></b> [diffusers](https://github.com/huggingface/diffusers)) - A library that provides pre-trained diffusion models for generating and editing images, audio, and video.
  - <b><code>158531⭐</code></b> <b><code>&nbsp;32673🍴</code></b> [transformers](https://github.com/huggingface/transformers)) - A framework that lets you easily use pre-trained transformer models for NLP, vision, and audio tasks.
  - <b><code>&nbsp;58593⭐</code></b> <b><code>&nbsp;&nbsp;4960🍴</code></b> [unsloth](https://github.com/unslothai/unsloth)) - A library for faster LLM fine-tuning and training with reduced memory usage.
  - <b><code>&nbsp;74652⭐</code></b> <b><code>&nbsp;14930🍴</code></b> [vllm](https://github.com/vllm-project/vllm)) - A high-throughput and memory-efficient inference and serving engine for LLMs.

## Deep Learning

_Frameworks for Neural Networks and Deep Learning. Also see <b><code>&nbsp;27786⭐</code></b> <b><code>&nbsp;&nbsp;6294🍴</code></b> [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning))._

- <b><code>&nbsp;35249⭐</code></b> <b><code>&nbsp;&nbsp;3493🍴</code></b> [jax](https://github.com/jax-ml/jax)) - A library for high-performance numerical computing with automatic differentiation and JIT compilation.
- <b><code>&nbsp;63916⭐</code></b> <b><code>&nbsp;19744🍴</code></b> [keras](https://github.com/keras-team/keras)) - A high-level deep learning library with support for JAX, TensorFlow, and PyTorch backends.
- <b><code>&nbsp;30975⭐</code></b> <b><code>&nbsp;&nbsp;3695🍴</code></b> [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)) - Deep learning framework to train, deploy, and ship AI products Lightning fast.
- <b><code>&nbsp;98635⭐</code></b> <b><code>&nbsp;27339🍴</code></b> [pytorch](https://github.com/pytorch/pytorch)) - Tensors and Dynamic neural networks in Python with strong GPU acceleration.
- <b><code>&nbsp;12993⭐</code></b> <b><code>&nbsp;&nbsp;2095🍴</code></b> [stable-baselines3](https://github.com/DLR-RM/stable-baselines3)) - PyTorch implementations of Stable Baselines (deep) reinforcement learning algorithms.
- <b><code>194382⭐</code></b> <b><code>&nbsp;75255🍴</code></b> [tensorflow](https://github.com/tensorflow/tensorflow)) - The most popular Deep Learning framework created by Google.

## Machine Learning

_Libraries for Machine Learning. Also see <b><code>&nbsp;72115⭐</code></b> <b><code>&nbsp;15374🍴</code></b> [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python))._

- <b><code>&nbsp;&nbsp;8866⭐</code></b> <b><code>&nbsp;&nbsp;1276🍴</code></b> [catboost](https://github.com/catboost/catboost)) - A fast, scalable, high performance gradient boosting on decision trees library.
- <b><code>&nbsp;&nbsp;2219⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;339🍴</code></b> [feature_engine](https://github.com/feature-engine/feature_engine)) - sklearn compatible API with the widest toolset for feature engineering and selection.
- <b><code>&nbsp;&nbsp;7524⭐</code></b> <b><code>&nbsp;&nbsp;2033🍴</code></b> [h2o](https://github.com/h2oai/h2o-3)) - Open Source Fast Scalable Machine Learning Platform.
- <b><code>&nbsp;18204⭐</code></b> <b><code>&nbsp;&nbsp;3988🍴</code></b> [lightgbm](https://github.com/lightgbm-org/LightGBM)) - A fast, distributed, high performance gradient boosting framework.
- <b><code>&nbsp;38866⭐</code></b> <b><code>&nbsp;&nbsp;6170🍴</code></b> [mindsdb](https://github.com/mindsdb/mindsdb)) - MindsDB is an open source AI layer for existing databases that allows you to effortlessly develop, train and deploy state-of-the-art machine learning models using standard queries.
- <b><code>&nbsp;&nbsp;3231⭐</code></b> <b><code>&nbsp;&nbsp;1100🍴</code></b> [pgmpy](https://github.com/pgmpy/pgmpy)) - A Python library for probabilistic graphical models and Bayesian networks.
- <b><code>&nbsp;65546⭐</code></b> <b><code>&nbsp;26861🍴</code></b> [scikit-learn](https://github.com/scikit-learn/scikit-learn)) - The most popular Python library for Machine Learning with extensive documentation and community support.
- <b><code>&nbsp;43056⭐</code></b> <b><code>&nbsp;29140🍴</code></b> [spark.ml](https://github.com/apache/spark)) - 🌎 [Apache Spark](spark.apache.org/)'s scalable 🌎 [Machine Learning library](spark.apache.org/docs/latest/ml-guide.html) for distributed computing.
- <b><code>&nbsp;&nbsp;&nbsp;566⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;84🍴</code></b> [TabGAN](https://github.com/Diyago/Tabular-data-generation)) - Synthetic tabular data generation using GANs, Diffusion Models, and LLMs.
- <b><code>&nbsp;28189⭐</code></b> <b><code>&nbsp;&nbsp;8860🍴</code></b> [xgboost](https://github.com/dmlc/xgboost)) - A scalable, portable, and distributed gradient boosting library.

## Natural Language Processing

_Libraries for working with human languages._

- General
  - <b><code>&nbsp;16381⭐</code></b> <b><code>&nbsp;&nbsp;4409🍴</code></b> [gensim](https://github.com/piskvorky/gensim)) - Topic Modeling for Humans.
  - <b><code>&nbsp;14575⭐</code></b> <b><code>&nbsp;&nbsp;3004🍴</code></b> [nltk](https://github.com/nltk/nltk)) - A leading platform for building Python programs to work with human language data.
  - <b><code>&nbsp;33396⭐</code></b> <b><code>&nbsp;&nbsp;4665🍴</code></b> [spacy](https://github.com/explosion/spaCy)) - A library for industrial-strength natural language processing in Python and Cython.
  - <b><code>&nbsp;&nbsp;7754⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;942🍴</code></b> [stanza](https://github.com/stanfordnlp/stanza)) - The Stanford NLP Group's official Python library, supporting 60+ languages.
- Chinese
  - <b><code>&nbsp;79677⭐</code></b> <b><code>&nbsp;15146🍴</code></b> [funnlp](https://github.com/fighting41love/funNLP)) - A collection of tools and datasets for Chinese NLP.

## Computer Vision

_Libraries for Computer Vision._

- <b><code>&nbsp;29187⭐</code></b> <b><code>&nbsp;&nbsp;3545🍴</code></b> [easyocr](https://github.com/JaidedAI/EasyOCR)) - Ready-to-use OCR with 40+ languages supported.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [kornia](https://github.com/kornia/kornia/)) - Open Source Differentiable Computer Vision Library for PyTorch.
- <b><code>&nbsp;&nbsp;5221⭐</code></b> <b><code>&nbsp;&nbsp;1004🍴</code></b> [opencv](https://github.com/opencv/opencv-python)) - Open Source Computer Vision Library.
- <b><code>&nbsp;&nbsp;6327⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;753🍴</code></b> [pytesseract](https://github.com/madmaze/pytesseract)) - A wrapper for [Google Tesseract OCR](https://github.com/tesseract-ocr).

## Recommender Systems

_Libraries for building recommender systems._

- <b><code>&nbsp;14192⭐</code></b> <b><code>&nbsp;&nbsp;1220🍴</code></b> [annoy](https://github.com/spotify/annoy)) - Approximate Nearest Neighbors in C++/Python optimized for memory usage.
- <b><code>&nbsp;&nbsp;3779⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;626🍴</code></b> [implicit](https://github.com/benfred/implicit)) - A fast Python implementation of collaborative filtering for implicit datasets.
- <b><code>&nbsp;&nbsp;6780⭐</code></b> <b><code>&nbsp;&nbsp;1051🍴</code></b> [scikit-surprise](https://github.com/NicolasHug/Surprise)) - A scikit for building and analyzing recommender systems.

**Web Development**

## Web Frameworks

_Traditional full stack web frameworks. Also see [Web APIs](#web-apis)._

- Synchronous
  - <b><code>&nbsp;&nbsp;8770⭐</code></b> <b><code>&nbsp;&nbsp;1501🍴</code></b> [bottle](https://github.com/bottlepy/bottle)) - A fast and simple micro-framework distributed as a single file with no dependencies.
  - <b><code>&nbsp;87129⭐</code></b> <b><code>&nbsp;33808🍴</code></b> [django](https://github.com/django/django)) - The most popular web framework in Python.
    - <b><code>&nbsp;&nbsp;1901⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;286🍴</code></b> [awesome-django](https://github.com/shahraizali/awesome-django))
  - <b><code>&nbsp;71354⭐</code></b> <b><code>&nbsp;16758🍴</code></b> [flask](https://github.com/pallets/flask)) - A microframework for Python.
    - <b><code>&nbsp;12704⭐</code></b> <b><code>&nbsp;&nbsp;1577🍴</code></b> [awesome-flask](https://github.com/humiaozuzu/awesome-flask))
  - <b><code>&nbsp;&nbsp;4079⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;895🍴</code></b> [pyramid](https://github.com/Pylons/pyramid)) - A small, fast, down-to-earth, open source Python web framework.
    - <b><code>&nbsp;&nbsp;&nbsp;570⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;56🍴</code></b> [awesome-pyramid](https://github.com/uralbash/awesome-pyramid))
  - <b><code>&nbsp;&nbsp;6898⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;303🍴</code></b> [fasthtml](https://github.com/AnswerDotAI/fasthtml)) - The fastest way to create an HTML app.
    - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;79⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [awesome-fasthtml](https://github.com/amosgyamfi/awesome-fasthtml))
  - <b><code>&nbsp;&nbsp;2364⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;135🍴</code></b> [masonite](https://github.com/MasoniteFramework/masonite)) - The modern and developer centric Python web framework.
- Asynchronous
  - <b><code>&nbsp;&nbsp;8123⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;527🍴</code></b> [litestar](https://github.com/litestar-org/litestar)) - Production-ready, capable and extensible ASGI Web framework.
  - <b><code>&nbsp;&nbsp;2096⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [microdot](https://github.com/miguelgrinberg/microdot)) - The impossibly small web framework for Python and MicroPython.
  - <b><code>&nbsp;28269⭐</code></b> <b><code>&nbsp;&nbsp;1699🍴</code></b> [reflex](https://github.com/reflex-dev/reflex)) - A framework for building reactive, full-stack web applications entirely with Python.
  - <b><code>&nbsp;&nbsp;7182⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;329🍴</code></b> [robyn](https://github.com/sparckles/Robyn)) - A high-performance async Python web framework with a Rust runtime.
  - <b><code>&nbsp;12143⭐</code></b> <b><code>&nbsp;&nbsp;1147🍴</code></b> [starlette](https://github.com/Kludex/starlette)) - A lightweight ASGI framework and toolkit for building high-performance async services.
  - <b><code>&nbsp;22410⭐</code></b> <b><code>&nbsp;&nbsp;5546🍴</code></b> [tornado](https://github.com/tornadoweb/tornado)) - A web framework and asynchronous networking library.

## Web APIs

_Libraries for building RESTful and GraphQL APIs._

- Django
  - <b><code>&nbsp;&nbsp;8980⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;567🍴</code></b> [django-ninja](https://github.com/vitalik/django-ninja)) - Fast, Django REST framework based on type hints and Pydantic.
  - <b><code>&nbsp;29941⭐</code></b> <b><code>&nbsp;&nbsp;7075🍴</code></b> [django-rest-framework](https://github.com/encode/django-rest-framework)) - A powerful and flexible toolkit to build web APIs.
  - <b><code>&nbsp;&nbsp;&nbsp;488⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;148🍴</code></b> [strawberry-django](https://github.com/strawberry-graphql/strawberry-django)) - Strawberry GraphQL integration with Django.
- Flask
  - <b><code>&nbsp;&nbsp;1124⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;140🍴</code></b> [apiflask](https://github.com/apiflask/apiflask)) - A lightweight Python web API framework based on Flask and Marshmallow.
- Framework Agnostic
  - <b><code>&nbsp;&nbsp;4577⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;783🍴</code></b> [connexion](https://github.com/spec-first/connexion)) - A spec-first framework that automatically handles requests based on your OpenAPI specification.
  - <b><code>&nbsp;&nbsp;9803⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;982🍴</code></b> [falcon](https://github.com/falconry/falcon)) - A high-performance framework for building cloud APIs and web app backends.
  - <b><code>&nbsp;96665⭐</code></b> <b><code>&nbsp;&nbsp;8965🍴</code></b> [fastapi](https://github.com/fastapi/fastapi)) - A modern, fast, web framework for building APIs with standard Python type hints.
  - <b><code>&nbsp;18640⭐</code></b> <b><code>&nbsp;&nbsp;1587🍴</code></b> [sanic](https://github.com/sanic-org/sanic)) - A Python 3.6+ web server and web framework that's written to go fast.
  - <b><code>&nbsp;&nbsp;4632⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;621🍴</code></b> [strawberry](https://github.com/strawberry-graphql/strawberry)) - A GraphQL library that leverages Python type annotations for schema definition.
  - <b><code>&nbsp;&nbsp;1404⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;161🍴</code></b> [webargs](https://github.com/marshmallow-code/webargs)) - A friendly library for parsing HTTP request arguments with built-in support for popular web frameworks.

## Web Servers

_ASGI and WSGI compatible web servers._

- ASGI
  - <b><code>&nbsp;&nbsp;2655⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;287🍴</code></b> [daphne](https://github.com/django/daphne)) - A HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP.
  - <b><code>&nbsp;&nbsp;5194⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;150🍴</code></b> [granian](https://github.com/emmett-framework/granian)) - A Rust HTTP server for Python applications built on top of Hyper and Tokio, supporting WSGI/ASGI/RSGI.
  - <b><code>&nbsp;&nbsp;1541⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;138🍴</code></b> [hypercorn](https://github.com/pgjones/hypercorn)) - An ASGI and WSGI Server based on Hyper libraries and inspired by Gunicorn.
  - <b><code>&nbsp;10546⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;926🍴</code></b> [uvicorn](https://github.com/Kludex/uvicorn)) - A lightning-fast ASGI server implementation, using uvloop and httptools.
- WSGI
  - <b><code>&nbsp;10502⭐</code></b> <b><code>&nbsp;&nbsp;1829🍴</code></b> [gunicorn](https://github.com/benoitc/gunicorn)) - Pre-forked, ported from Ruby's Unicorn project.
  - <b><code>&nbsp;&nbsp;3543⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;695🍴</code></b> [uwsgi](https://github.com/unbit/uwsgi)) - A project aims at developing a full stack for building hosting services, written in C.
  - <b><code>&nbsp;&nbsp;1572⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;179🍴</code></b> [waitress](https://github.com/Pylons/waitress)) - Multi-threaded, powers Pyramid.
- RPC
  - <b><code>&nbsp;44563⭐</code></b> <b><code>&nbsp;11096🍴</code></b> [grpcio](https://github.com/grpc/grpc)) - HTTP/2-based RPC framework with Python bindings, built by Google.
  - <b><code>&nbsp;&nbsp;1695⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;250🍴</code></b> [rpyc](https://github.com/tomerfiliba-org/rpyc)) (Remote Python Call) - A transparent and symmetric RPC library for Python.

## WebSocket

_Libraries for working with WebSocket._

- <b><code>&nbsp;&nbsp;2534⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;769🍴</code></b> [autobahn-python](https://github.com/crossbario/autobahn-python)) - WebSocket & WAMP for Python on Twisted and 🌎 [asyncio](docs.python.org/3/library/asyncio.html).
- <b><code>&nbsp;&nbsp;6335⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;820🍴</code></b> [channels](https://github.com/django/channels)) - Developer-friendly asynchrony for Django.
- <b><code>&nbsp;&nbsp;5507⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;897🍴</code></b> [flask-socketio](https://github.com/miguelgrinberg/Flask-SocketIO)) - Socket.IO integration for Flask applications.
- <b><code>&nbsp;&nbsp;5650⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;587🍴</code></b> [websockets](https://github.com/python-websockets/websockets)) - A library for building WebSocket servers and clients with a focus on correctness and simplicity.

## Template Engines

_Libraries and tools for templating and lexing._

- <b><code>&nbsp;11533⭐</code></b> <b><code>&nbsp;&nbsp;1719🍴</code></b> [jinja](https://github.com/pallets/jinja)) - A modern and designer friendly templating language.
- <b><code>&nbsp;&nbsp;&nbsp;430⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;69🍴</code></b> [mako](https://github.com/sqlalchemy/mako)) - Hyperfast and lightweight templating for the Python platform.

## Web Asset Management

_Tools for managing, compressing and minifying website assets._

- <b><code>&nbsp;&nbsp;2873⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;609🍴</code></b> [django-compressor](https://github.com/django-compressor/django-compressor)) - Compresses linked and inline JavaScript or CSS into a single cached file.
- <b><code>&nbsp;&nbsp;2943⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;887🍴</code></b> [django-storages](https://github.com/jschneier/django-storages)) - A collection of custom storage back ends for Django.

## Authentication

_Libraries for implementing authentication schemes._

- OAuth
  - <b><code>&nbsp;&nbsp;5255⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;525🍴</code></b> [authlib](https://github.com/authlib/authlib)) - JavaScript Object Signing and Encryption draft implementation.
  - <b><code>&nbsp;10312⭐</code></b> <b><code>&nbsp;&nbsp;3118🍴</code></b> [django-allauth](https://github.com/pennersr/django-allauth)) - Authentication app for Django that "just works."
  - <b><code>&nbsp;&nbsp;3313⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;836🍴</code></b> [django-oauth-toolkit](https://github.com/django-oauth/django-oauth-toolkit)) - OAuth 2 goodies for Django.
  - <b><code>&nbsp;&nbsp;2960⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;503🍴</code></b> [oauthlib](https://github.com/oauthlib/oauthlib)) - A generic and thorough implementation of the OAuth request-signing logic.
- JWT
  - <b><code>&nbsp;&nbsp;5632⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;747🍴</code></b> [pyjwt](https://github.com/jpadilla/pyjwt)) - JSON Web Token implementation in Python.
- Permissions
  - <b><code>&nbsp;&nbsp;3893⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;583🍴</code></b> [django-guardian](https://github.com/django-guardian/django-guardian)) - Implementation of per object permissions for Django 1.2+
  - <b><code>&nbsp;&nbsp;1971⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;150🍴</code></b> [django-rules](https://github.com/dfunckt/django-rules)) - A tiny but powerful app providing object-level permissions to Django, without requiring a database.

## Admin Panels

_Libraries for administrative interfaces._

- <b><code>&nbsp;&nbsp;7908⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;870🍴</code></b> [ajenti](https://github.com/ajenti/ajenti)) - The admin panel your servers deserve.
- <b><code>&nbsp;&nbsp;3927⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;655🍴</code></b> [django-grappelli](https://github.com/sehmaschine/django-grappelli)) - A jazzy skin for the Django Admin-Interface.
- <b><code>&nbsp;&nbsp;3383⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;334🍴</code></b> [django-unfold](https://github.com/unfoldadmin/django-unfold)) - Elevate your Django admin with a stunning modern interface, powerful features, and seamless user experience.
- <b><code>&nbsp;&nbsp;6057⭐</code></b> <b><code>&nbsp;&nbsp;1632🍴</code></b> [flask-admin](https://github.com/pallets-eco/flask-admin)) - Simple and extensible administrative interface framework for Flask.
- <b><code>&nbsp;&nbsp;7137⭐</code></b> <b><code>&nbsp;&nbsp;1146🍴</code></b> [flower](https://github.com/mher/flower)) - Real-time monitor and web admin for Celery.
- <b><code>&nbsp;&nbsp;&nbsp;396⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;19🍴</code></b> [func-to-web](https://github.com/offerrall/FuncToWeb)) - Instantly create web UIs from Python functions using type hints. Zero frontend code required.
- <b><code>&nbsp;&nbsp;1796⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;168🍴</code></b> [jet-bridge](https://github.com/jet-admin/jet-bridge)) - Admin panel framework for any application with nice UI (ex Jet Django).

## CMS

_Content Management Systems._

- <b><code>&nbsp;10640⭐</code></b> <b><code>&nbsp;&nbsp;3196🍴</code></b> [django-cms](https://github.com/django-cms/django-cms)) - The easy-to-use and developer-friendly enterprise CMS powered by Django.
- <b><code>&nbsp;&nbsp;2042⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;520🍴</code></b> [indico](https://github.com/indico/indico)) - A feature-rich event management system, made @ 🌎 [CERN](en.wikipedia.org/wiki/CERN).
- <b><code>&nbsp;20272⭐</code></b> <b><code>&nbsp;&nbsp;4508🍴</code></b> [wagtail](https://github.com/wagtail/wagtail)) - A Django content management system.

## Static Site Generators

_Static site generator is a software that takes some text + templates as input and produces HTML files on the output._

- <b><code>&nbsp;&nbsp;3926⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;317🍴</code></b> [lektor](https://github.com/lektor/lektor)) - An easy to use static CMS and blog engine.
- <b><code>&nbsp;&nbsp;2726⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;466🍴</code></b> [nikola](https://github.com/getnikola/nikola)) - A static website and blog generator.
- <b><code>&nbsp;13261⭐</code></b> <b><code>&nbsp;&nbsp;1830🍴</code></b> [pelican](https://github.com/getpelican/pelican)) - Static site generator that supports Markdown and reST syntax.

**HTTP & Scraping**

## HTTP Clients

_Libraries for working with HTTP._

- <b><code>&nbsp;16356⭐</code></b> <b><code>&nbsp;&nbsp;2233🍴</code></b> [aiohttp](https://github.com/aio-libs/aiohttp)) - Asynchronous HTTP client/server framework for asyncio and Python.
- <b><code>&nbsp;&nbsp;2799⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;157🍴</code></b> [furl](https://github.com/gruns/furl)) - A small Python library that makes parsing and manipulating URLs easy.
- <b><code>&nbsp;15131⭐</code></b> <b><code>&nbsp;&nbsp;1093🍴</code></b> [httpx](https://github.com/encode/httpx)) - A next generation HTTP client for Python.
- <b><code>&nbsp;53850⭐</code></b> <b><code>&nbsp;&nbsp;9806🍴</code></b> [requests](https://github.com/psf/requests)) - HTTP Requests for Humans.
- <b><code>&nbsp;&nbsp;4012⭐</code></b> <b><code>&nbsp;&nbsp;1307🍴</code></b> [urllib3](https://github.com/urllib3/urllib3)) - A HTTP library with thread-safe connection pooling, file post support, sanity friendly.

## Web Scraping

_Libraries to automate web scraping and extract web content._

- Frameworks
  - <b><code>&nbsp;84948⭐</code></b> <b><code>&nbsp;&nbsp;9837🍴</code></b> [browser-use](https://github.com/browser-use/browser-use)) - Make websites accessible for AI agents with easy browser automation.
  - <b><code>&nbsp;62875⭐</code></b> <b><code>&nbsp;&nbsp;6410🍴</code></b> [crawl4ai](https://github.com/unclecode/crawl4ai)) - An open-source, LLM-friendly web crawler that provides lightning-fast, structured data extraction specifically designed for AI agents.
  - <b><code>&nbsp;&nbsp;4849⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;387🍴</code></b> [mechanicalsoup](https://github.com/MechanicalSoup/MechanicalSoup)) - A Python library for automating interaction with websites.
  - <b><code>&nbsp;60987⭐</code></b> <b><code>&nbsp;11400🍴</code></b> [scrapy](https://github.com/scrapy/scrapy)) - A fast high-level screen scraping and web crawling framework.
- Content Extraction
  - <b><code>&nbsp;&nbsp;2337⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;353🍴</code></b> [feedparser](https://github.com/kurtmckee/feedparser)) - Universal feed parser.
  - <b><code>&nbsp;&nbsp;2138⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;292🍴</code></b> [html2text](https://github.com/Alir3z4/html2text)) - Convert HTML to Markdown-formatted text.
  - <b><code>&nbsp;&nbsp;&nbsp;674⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;89🍴</code></b> [micawber](https://github.com/coleifer/micawber)) - A small library for extracting rich content from URLs.
  - <b><code>&nbsp;&nbsp;3668⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;541🍴</code></b> [sumy](https://github.com/miso-belica/sumy)) - A module for automatic summarization of text documents and HTML pages.
  - <b><code>&nbsp;&nbsp;5612⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;352🍴</code></b> [trafilatura](https://github.com/adbar/trafilatura)) - A tool for gathering text and metadata from the web, with built-in content filtering.

## Email

_Libraries for sending and parsing email, and mail server management._

- <b><code>&nbsp;&nbsp;3474⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;462🍴</code></b> [modoboa](https://github.com/modoboa/modoboa)) - A mail hosting and management platform including a modern Web UI.
- <b><code>&nbsp;&nbsp;2725⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;266🍴</code></b> [yagmail](https://github.com/kootenpv/yagmail)) - Yet another Gmail/SMTP client.

**Database & Storage**

## ORM

_Libraries that implement Object-Relational Mapping or data mapping techniques._

- Relational Databases
  - <b><code>&nbsp;87129⭐</code></b> <b><code>&nbsp;33808🍴</code></b> [django.db.models](https://github.com/django/django)) - The Django 🌎 [ORM](docs.djangoproject.com/en/dev/topics/db/models/).
  - <b><code>&nbsp;11683⭐</code></b> <b><code>&nbsp;&nbsp;1662🍴</code></b> [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)) - The Python SQL Toolkit and Object Relational Mapper.
    - <b><code>&nbsp;&nbsp;3037⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;156🍴</code></b> [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy))
  - <b><code>&nbsp;&nbsp;4854⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;296🍴</code></b> [dataset](https://github.com/pudo/dataset)) - Store Python dicts in a database - works with SQLite, MySQL, and PostgreSQL.
  - <b><code>&nbsp;11958⭐</code></b> <b><code>&nbsp;&nbsp;1389🍴</code></b> [peewee](https://github.com/coleifer/peewee)) - A small, expressive ORM.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [pony](https://github.com/ponyorm/pony/)) - ORM that provides a generator-oriented interface to SQL.
  - <b><code>&nbsp;17762⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;826🍴</code></b> [sqlmodel](https://github.com/fastapi/sqlmodel)) - SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.
  - <b><code>&nbsp;&nbsp;5534⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;470🍴</code></b> [tortoise-orm](https://github.com/tortoise/tortoise-orm)) - An easy-to-use asyncio ORM inspired by Django, with relations support.
- NoSQL Databases
  - <b><code>&nbsp;&nbsp;2666⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;283🍴</code></b> [beanie](https://github.com/BeanieODM/beanie)) - An asynchronous Python object-document mapper (ODM) for MongoDB.
  - <b><code>&nbsp;&nbsp;4349⭐</code></b> <b><code>&nbsp;&nbsp;1231🍴</code></b> [mongoengine](https://github.com/MongoEngine/mongoengine)) - A Python Object-Document-Mapper for working with MongoDB.
  - <b><code>&nbsp;&nbsp;2646⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;426🍴</code></b> [pynamodb](https://github.com/pynamodb/PynamoDB)) - A Pythonic interface for 🌎 [Amazon DynamoDB](aws.amazon.com/dynamodb/).

## Database Drivers

_Libraries for connecting and operating databases._

- MySQL - <b><code>&nbsp;&nbsp;2558⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;396🍴</code></b> [awesome-mysql](https://github.com/shlomi-noach/awesome-mysql))
  - <b><code>&nbsp;&nbsp;2523⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;444🍴</code></b> [mysqlclient](https://github.com/PyMySQL/mysqlclient)) - MySQL connector with Python 3 support  🌎 [mysql-python](sourceforge.net/projects/mysql-python/) fork).
  - <b><code>&nbsp;&nbsp;7836⭐</code></b> <b><code>&nbsp;&nbsp;1439🍴</code></b> [pymysql](https://github.com/PyMySQL/PyMySQL)) - A pure Python MySQL driver compatible to mysql-python.
- PostgreSQL - <b><code>&nbsp;11797⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;947🍴</code></b> [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres))
  - <b><code>&nbsp;&nbsp;2333⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;223🍴</code></b> [psycopg](https://github.com/psycopg/psycopg)) - The most popular PostgreSQL adapter for Python.
- SQlite - <b><code>&nbsp;&nbsp;&nbsp;391⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;44🍴</code></b> [awesome-sqlite](https://github.com/planetopendata/awesome-sqlite))
  - <b><code>&nbsp;&nbsp;2023⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;129🍴</code></b> [sqlite-utils](https://github.com/simonw/sqlite-utils)) - Python CLI utility and library for manipulating SQLite databases.
  - 🌎 [sqlite3](docs.python.org/3/library/sqlite3.html) - (Python standard library) SQlite interface compliant with DB-API 2.0.
- Other Relational Databases
  - <b><code>&nbsp;&nbsp;1293⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;228🍴</code></b> [clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver)) - Python driver with native interface for ClickHouse.
  - <b><code>&nbsp;&nbsp;&nbsp;404⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;42🍴</code></b> [mssql-python](https://github.com/microsoft/mssql-python)) - Official Microsoft driver for SQL Server and Azure SQL, built on ODBC for high performance and low memory usage.
- NoSQL Databases
  - <b><code>&nbsp;&nbsp;1426⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;573🍴</code></b> [cassandra-driver](https://github.com/apache/cassandra-python-driver)) - The Python Driver for Apache Cassandra.
  - <b><code>&nbsp;&nbsp;&nbsp;218⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;31🍴</code></b> [django-mongodb-backend](https://github.com/mongodb/django-mongodb-backend)) - Official MongoDB database backend for Django.
  - <b><code>&nbsp;&nbsp;4342⭐</code></b> <b><code>&nbsp;&nbsp;1141🍴</code></b> [pymongo](https://github.com/mongodb/mongo-python-driver)) - The official Python client for MongoDB.
  - <b><code>&nbsp;13528⭐</code></b> <b><code>&nbsp;&nbsp;2669🍴</code></b> [redis-py](https://github.com/redis/redis-py)) - The Python client for Redis.

## Database

_Databases implemented in Python._

- <b><code>&nbsp;27026⭐</code></b> <b><code>&nbsp;&nbsp;2158🍴</code></b> [chromadb](https://github.com/chroma-core/chroma)) - An open-source embedding database for building AI applications with embeddings and semantic search.
- <b><code>&nbsp;37043⭐</code></b> <b><code>&nbsp;&nbsp;3047🍴</code></b> [duckdb](https://github.com/duckdb/duckdb)) - An in-process SQL OLAP database management system; optimized for analytics and fast queries, similar to SQLite but for analytical workloads.
- <b><code>&nbsp;&nbsp;1069⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;133🍴</code></b> [pickledb](https://github.com/patx/pickledb)) - A simple and lightweight key-value store for Python.
- <b><code>&nbsp;&nbsp;7494⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;604🍴</code></b> [tinydb](https://github.com/msiemens/tinydb)) - A tiny, document-oriented database.
- <b><code>&nbsp;&nbsp;&nbsp;752⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;100🍴</code></b> [ZODB](https://github.com/zopefoundation/ZODB)) - A native object database for Python. A key-value and object graph database.

## Caching

_Libraries for caching data._

- <b><code>&nbsp;&nbsp;2718⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;187🍴</code></b> [cachetools](https://github.com/tkem/cachetools)) - Extensible memoizing collections and decorators.
- <b><code>&nbsp;&nbsp;2265⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;235🍴</code></b> [django-cacheops](https://github.com/Suor/django-cacheops)) - A slick ORM cache with automatic granular event-driven invalidation.
- <b><code>&nbsp;&nbsp;&nbsp;293⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [dogpile.cache](https://github.com/sqlalchemy/dogpile.cache)) - dogpile.cache is a next generation replacement for Beaker made by the same authors.
- <b><code>&nbsp;&nbsp;2851⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;158🍴</code></b> [python-diskcache](https://github.com/grantjenks/python-diskcache)) - SQLite and file backed cache backend with faster lookups than memcached and redis.

## Search

_Libraries and software for indexing and performing search queries on data._

- <b><code>&nbsp;&nbsp;3800⭐</code></b> <b><code>&nbsp;&nbsp;1311🍴</code></b> [django-haystack](https://github.com/django-haystack/django-haystack)) - Modular search for Django.
- <b><code>&nbsp;&nbsp;4373⭐</code></b> <b><code>&nbsp;&nbsp;1203🍴</code></b> [elasticsearch-py](https://github.com/elastic/elasticsearch-py)) - The official low-level Python client for 🌎 [Elasticsearch](www.elastic.co/products/elasticsearch).
- <b><code>&nbsp;&nbsp;&nbsp;697⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;338🍴</code></b> [pysolr](https://github.com/django-haystack/pysolr)) - A lightweight Python wrapper for 🌎 [Apache Solr](lucene.apache.org/solr/).

## Serialization

_Libraries for serializing complex data types._

- <b><code>&nbsp;&nbsp;7229⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;678🍴</code></b> [marshmallow](https://github.com/marshmallow-code/marshmallow)) - A lightweight library for converting complex objects to and from simple Python datatypes.
- <b><code>&nbsp;&nbsp;2073⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;241🍴</code></b> [msgpack](https://github.com/msgpack/msgpack-python)) - MessagePack serializer implementation for Python.
- <b><code>&nbsp;&nbsp;7990⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;298🍴</code></b> [orjson](https://github.com/ijl/orjson)) - Fast, correct JSON library.

**Data & Science**

## Data Analysis

_Libraries for data analysis._

- General
  - <b><code>&nbsp;&nbsp;4107⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;722🍴</code></b> [aws-sdk-pandas](https://github.com/aws/aws-sdk-pandas)) - Pandas on AWS.
  - <b><code>&nbsp;10890⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;814🍴</code></b> [datasette](https://github.com/simonw/datasette)) - An open source multi-tool for exploring and publishing data.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [desbordante](https://github.com/desbordante/desbordante-core/)) - An open source data profiler for complex pattern discovery.
  - <b><code>&nbsp;&nbsp;6474⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;713🍴</code></b> [ibis](https://github.com/ibis-project/ibis)) - A portable Python dataframe library with a single API for 20+ backends.
  - <b><code>&nbsp;10365⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;674🍴</code></b> [modin](https://github.com/modin-project/modin)) - A drop-in pandas replacement that scales workflows by changing a single line of code.
  - <b><code>&nbsp;48274⭐</code></b> <b><code>&nbsp;19792🍴</code></b> [pandas](https://github.com/pandas-dev/pandas)) - A library providing high-performance, easy-to-use data structures and data analysis tools.
  - <b><code>&nbsp;63107⭐</code></b> <b><code>&nbsp;&nbsp;1628🍴</code></b> [pathway](https://github.com/pathwaycom/pathway)) - Real-time data processing framework for Python with reactive dataflows.
  - <b><code>&nbsp;37908⭐</code></b> <b><code>&nbsp;&nbsp;2712🍴</code></b> [polars](https://github.com/pola-rs/polars)) - A fast DataFrame library implemented in Rust with a Python API.
- Financial Data
  - <b><code>&nbsp;17827⭐</code></b> <b><code>&nbsp;&nbsp;2990🍴</code></b> [akshare](https://github.com/akfamily/akshare)) - A financial data interface library, built for human beings!
  - <b><code>&nbsp;&nbsp;1923⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;334🍴</code></b> [edgartools](https://github.com/dgunning/edgartools)) - Library for downloading structured data from SEC EDGAR filings and XBRL financial statements.
  - <b><code>&nbsp;64047⭐</code></b> <b><code>&nbsp;&nbsp;6310🍴</code></b> [openbb](https://github.com/OpenBB-finance/OpenBB)) - A financial data platform for analysts, quants and AI agents.
  - <b><code>&nbsp;22408⭐</code></b> <b><code>&nbsp;&nbsp;3125🍴</code></b> [yfinance](https://github.com/ranaroussi/yfinance)) - Easy Pythonic way to download market and financial data from Yahoo Finance.

## Data Validation

_Libraries for validating data. Used for forms in many cases._

- <b><code>&nbsp;&nbsp;3273⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;242🍴</code></b> [cerberus](https://github.com/pyeve/cerberus)) - A lightweight and extensible data validation library.
- <b><code>&nbsp;&nbsp;4940⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;611🍴</code></b> [jsonschema](https://github.com/python-jsonschema/jsonschema)) - An implementation of [JSON Schema](http://json-schema.org/) for Python.
- <b><code>&nbsp;&nbsp;4275⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;383🍴</code></b> [pandera](https://github.com/unionai-oss/pandera)) - A data validation library for dataframes, with support for pandas, polars, and Spark.
- <b><code>&nbsp;27312⭐</code></b> <b><code>&nbsp;&nbsp;2516🍴</code></b> [pydantic](https://github.com/pydantic/pydantic)) - Data validation using Python type hints.

## Data Visualization

_Libraries for visualizing data. Also see <b><code>&nbsp;34936⭐</code></b> <b><code>&nbsp;&nbsp;4527🍴</code></b> [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization))._

- Plotting
  - <b><code>&nbsp;10319⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;842🍴</code></b> [altair](https://github.com/vega/altair)) - Declarative statistical visualization library for Python.
  - <b><code>&nbsp;20388⭐</code></b> <b><code>&nbsp;&nbsp;4256🍴</code></b> [bokeh](https://github.com/bokeh/bokeh)) - Interactive Web Plotting for Python.
  - <b><code>&nbsp;&nbsp;3685⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;480🍴</code></b> [bqplot](https://github.com/bqplot/bqplot)) - Interactive Plotting Library for the Jupyter Notebook.
  - <b><code>&nbsp;22652⭐</code></b> <b><code>&nbsp;&nbsp;8299🍴</code></b> [matplotlib](https://github.com/matplotlib/matplotlib)) - A Python 2D plotting library.
  - <b><code>&nbsp;18400⭐</code></b> <b><code>&nbsp;&nbsp;2790🍴</code></b> [plotly](https://github.com/plotly/plotly.py)) - Interactive graphing library for Python.
  - <b><code>&nbsp;&nbsp;4531⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;243🍴</code></b> [plotnine](https://github.com/has2k1/plotnine)) - A grammar of graphics for Python based on ggplot2.
  - <b><code>&nbsp;&nbsp;2752⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;416🍴</code></b> [pygal](https://github.com/Kozea/pygal)) - A Python SVG Charts Creator.
  - <b><code>&nbsp;&nbsp;4322⭐</code></b> <b><code>&nbsp;&nbsp;1152🍴</code></b> [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph)) - Interactive and realtime 2D/3D/Image plotting and science/engineering widgets.
  - <b><code>&nbsp;13784⭐</code></b> <b><code>&nbsp;&nbsp;2091🍴</code></b> [seaborn](https://github.com/mwaskom/seaborn)) - Statistical data visualization using Matplotlib.
  - <b><code>&nbsp;&nbsp;&nbsp;284⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;23🍴</code></b> [ultraplot](https://github.com/ultraplot/UltraPlot)) - Matplotlib wrapper for publication-ready scientific figures with minimal code. Includes advanced subplot management, panel layouts, and batteries-included geoscience plotting.
  - <b><code>&nbsp;&nbsp;3559⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;629🍴</code></b> [vispy](https://github.com/vispy/vispy)) - High-performance scientific visualization based on OpenGL.
- Specialized
  - <b><code>&nbsp;&nbsp;1595⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;394🍴</code></b> [cartopy](https://github.com/SciTools/cartopy)) - A cartographic python library with matplotlib support.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [pygraphviz](https://github.com/pygraphviz/pygraphviz/)) - Python interface to [Graphviz](http://www.graphviz.org/).
- Dashboards and Apps
  - <b><code>&nbsp;42196⭐</code></b> <b><code>&nbsp;&nbsp;3360🍴</code></b> [gradio](https://github.com/gradio-app/gradio)) - Build and share machine learning apps, all in Python.
  - <b><code>&nbsp;44057⭐</code></b> <b><code>&nbsp;&nbsp;4175🍴</code></b> [streamlit](https://github.com/streamlit/streamlit)) - A framework which lets you build dashboards, generate reports, or create chat apps in minutes.

## Geolocation

_Libraries for geocoding addresses and working with latitudes and longitudes._

- <b><code>&nbsp;&nbsp;1523⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;302🍴</code></b> [django-countries](https://github.com/SmileyChris/django-countries)) - A Django app that provides a country field for models and forms.
- <b><code>&nbsp;87129⭐</code></b> <b><code>&nbsp;33808🍴</code></b> [geodjango](https://github.com/django/django)) - A world-class geographic web framework that is part of 🌎 [Django](docs.djangoproject.com/en/dev/ref/contrib/gis/).
- <b><code>&nbsp;&nbsp;&nbsp;984⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;129🍴</code></b> [geojson](https://github.com/jazzband/geojson)) - Python bindings and utilities for GeoJSON.
- <b><code>&nbsp;&nbsp;5077⭐</code></b> <b><code>&nbsp;&nbsp;1008🍴</code></b> [geopandas](https://github.com/geopandas/geopandas)) - Python tools for geographic data (GeoSeries/GeoDataFrame) built on pandas.
- <b><code>&nbsp;&nbsp;4792⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;661🍴</code></b> [geopy](https://github.com/geopy/geopy)) - Python Geocoding Toolbox.

## Science

_Libraries for scientific computing. Also see <b><code>&nbsp;&nbsp;&nbsp;356⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [Python-for-Scientists](https://github.com/TomNicholas/Python-for-Scientists))._

- Core
  - <b><code>&nbsp;10942⭐</code></b> <b><code>&nbsp;&nbsp;1243🍴</code></b> [numba](https://github.com/numba/numba)) - Python JIT compiler to LLVM aimed at scientific Python.
  - <b><code>&nbsp;31680⭐</code></b> <b><code>&nbsp;12213🍴</code></b> [numpy](https://github.com/numpy/numpy)) - A fundamental package for scientific computing with Python.
  - <b><code>&nbsp;14572⭐</code></b> <b><code>&nbsp;&nbsp;5677🍴</code></b> [scipy](https://github.com/scipy/scipy)) - A Python-based ecosystem of open-source software for mathematics, science, and engineering.
  - <b><code>&nbsp;11329⭐</code></b> <b><code>&nbsp;&nbsp;3326🍴</code></b> [statsmodels](https://github.com/statsmodels/statsmodels)) - Statistical modeling and econometrics in Python.
  - <b><code>&nbsp;14524⭐</code></b> <b><code>&nbsp;&nbsp;5238🍴</code></b> [sympy](https://github.com/sympy/sympy)) - A Python library for symbolic mathematics.
- Biology and Chemistry
  - <b><code>&nbsp;&nbsp;4940⭐</code></b> <b><code>&nbsp;&nbsp;1880🍴</code></b> [biopython](https://github.com/biopython/biopython)) - Biopython is a set of freely available tools for biological computation.
  - <b><code>&nbsp;&nbsp;&nbsp;398⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;177🍴</code></b> [cclib](https://github.com/cclib/cclib)) - A library for parsing and interpreting the results of computational chemistry packages.
  - <b><code>&nbsp;&nbsp;1295⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;469🍴</code></b> [openbabel](https://github.com/openbabel/openbabel)) - A chemical toolbox designed to speak the many languages of chemical data.
  - <b><code>&nbsp;&nbsp;3362⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;995🍴</code></b> [rdkit](https://github.com/rdkit/rdkit)) - Cheminformatics and Machine Learning Software.
- Physics and Engineering
  - <b><code>&nbsp;&nbsp;5099⭐</code></b> <b><code>&nbsp;&nbsp;2060🍴</code></b> [astropy](https://github.com/astropy/astropy)) - A community Python library for Astronomy.
  - <b><code>&nbsp;&nbsp;1290⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;561🍴</code></b> [obspy](https://github.com/obspy/obspy)) - A Python toolbox for seismology.
  - <b><code>&nbsp;&nbsp;&nbsp;409⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [pydy](https://github.com/pydy/pydy)) - Short for Python Dynamics, used to assist with workflow in the modeling of dynamic motion.
  - <b><code>&nbsp;29009⭐</code></b> <b><code>&nbsp;&nbsp;7249🍴</code></b> [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)) - This is a compilation of various robotics algorithms with visualizations.
- Simulation and Modeling
  - <b><code>&nbsp;&nbsp;&nbsp;339⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;32🍴</code></b> [pathsim](https://github.com/pathsim/pathsim)) - A block-based system modeling and simulation framework with a browser-based visual editor.
  - <b><code>&nbsp;&nbsp;9552⭐</code></b> <b><code>&nbsp;&nbsp;2243🍴</code></b> [pymc](https://github.com/pymc-devs/pymc)) - Probabilistic programming and Bayesian modeling in Python.
  - 🌎 [simpy](gitlab.com/team-simpy/simpy) - A process-based discrete-event simulation framework.
- Other
  - <b><code>&nbsp;&nbsp;2542⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;285🍴</code></b> [colour](https://github.com/colour-science/colour)) - Implementing a comprehensive number of colour theory transformations and algorithms.
  - <b><code>&nbsp;37459⭐</code></b> <b><code>&nbsp;&nbsp;2753🍴</code></b> [manim](https://github.com/ManimCommunity/manim)) - An animation engine for explanatory math videos.
  - <b><code>&nbsp;16770⭐</code></b> <b><code>&nbsp;&nbsp;3495🍴</code></b> [networkx](https://github.com/networkx/networkx)) - A high-productivity software for complex networks.
  - <b><code>&nbsp;&nbsp;4407⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;609🍴</code></b> [shapely](https://github.com/shapely/shapely)) - Manipulation and analysis of geometric objects in the Cartesian plane.

## Quantum Computing

_Libraries for quantum computing._

- <b><code>&nbsp;&nbsp;4904⭐</code></b> <b><code>&nbsp;&nbsp;1201🍴</code></b> [Cirq](https://github.com/quantumlib/Cirq)) — A Google-developed framework focused on hardware-aware quantum circuit design for NISQ devices.
- <b><code>&nbsp;&nbsp;3123⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;759🍴</code></b> [pennylane](https://github.com/PennyLaneAI/pennylane)) — A hybrid quantum-classical machine learning library with automatic differentiation support.
- <b><code>&nbsp;&nbsp;7185⭐</code></b> <b><code>&nbsp;&nbsp;2813🍴</code></b> [qiskit](https://github.com/Qiskit/qiskit)) — An IBM-backed quantum SDK for building, simulating, and running circuits on real quantum hardware.
- <b><code>&nbsp;&nbsp;1981⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;740🍴</code></b> [qutip](https://github.com/qutip/qutip)) - Quantum Toolbox in Python.

**Developer Tools**

## Algorithms and Design Patterns

_Python implementation of data structures, algorithms and design patterns. Also see <b><code>&nbsp;24912⭐</code></b> <b><code>&nbsp;&nbsp;2947🍴</code></b> [awesome-algorithms](https://github.com/tayllan/awesome-algorithms))._

- Algorithms
  - <b><code>&nbsp;25406⭐</code></b> <b><code>&nbsp;&nbsp;4732🍴</code></b> [algorithms](https://github.com/keon/algorithms)) - Minimal examples of data structures and algorithms.
  - <b><code>&nbsp;&nbsp;3935⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;225🍴</code></b> [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)) - Fast and pure-Python implementation of sorted collections.
  - <b><code>219112⭐</code></b> <b><code>&nbsp;50272🍴</code></b> [thealgorithms](https://github.com/TheAlgorithms/Python)) - All Algorithms implemented in Python.
- Design Patterns
  - <b><code>&nbsp;42810⭐</code></b> <b><code>&nbsp;&nbsp;7044🍴</code></b> [python-patterns](https://github.com/faif/python-patterns)) - A collection of design patterns in Python.
  - <b><code>&nbsp;&nbsp;6470⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;565🍴</code></b> [transitions](https://github.com/pytransitions/transitions)) - A lightweight, object-oriented finite state machine implementation.

## Interactive Interpreter

_Interactive Python interpreters (REPL)._

- <b><code>&nbsp;13039⭐</code></b> <b><code>&nbsp;&nbsp;5629🍴</code></b> [jupyter](https://github.com/jupyter/notebook)) - A rich toolkit to help you make the most out of using Python interactively.
  - <b><code>&nbsp;&nbsp;4574⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;455🍴</code></b> [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter))
- <b><code>&nbsp;19995⭐</code></b> <b><code>&nbsp;&nbsp;1001🍴</code></b> [marimo](https://github.com/marimo-team/marimo)) - Transform data and train models, feels like a next-gen notebook, stored as Git-friendly Python.
- <b><code>&nbsp;&nbsp;5413⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;290🍴</code></b> [ptpython](https://github.com/prompt-toolkit/ptpython)) - Advanced Python REPL built on top of the <b><code>&nbsp;10348⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;774🍴</code></b> [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)).

## Code Analysis

_Tools of static analysis, linters and code quality checkers. Also see <b><code>&nbsp;14461⭐</code></b> <b><code>&nbsp;&nbsp;1445🍴</code></b> [awesome-static-analysis](https://github.com/analysis-tools-dev/static-analysis))._

- Code Analysis
  - <b><code>&nbsp;&nbsp;4554⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;329🍴</code></b> [code2flow](https://github.com/scottrogowski/code2flow)) - Turn your Python and JavaScript code into DOT flowcharts.
  - <b><code>&nbsp;&nbsp;2075⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;178🍴</code></b> [prospector](https://github.com/prospector-dev/prospector)) - A tool to analyze Python code.
  - <b><code>&nbsp;&nbsp;4410⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;179🍴</code></b> [vulture](https://github.com/jendrikseipp/vulture)) - A tool for finding and analyzing dead Python code.
- Code Linters
  - <b><code>&nbsp;&nbsp;7889⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;745🍴</code></b> [bandit](https://github.com/PyCQA/bandit)) - A tool designed to find common security issues in Python code.
  - <b><code>&nbsp;&nbsp;3772⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;343🍴</code></b> [flake8](https://github.com/PyCQA/flake8)) - A wrapper around `pycodestyle`, `pyflakes` and McCabe.
    - <b><code>&nbsp;&nbsp;1273⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51🍴</code></b> [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions))
  - <b><code>&nbsp;&nbsp;5666⭐</code></b> <b><code>&nbsp;&nbsp;1232🍴</code></b> [pylint](https://github.com/pylint-dev/pylint)) - A fully customizable source code analyzer.
  - <b><code>&nbsp;46742⭐</code></b> <b><code>&nbsp;&nbsp;1973🍴</code></b> [ruff](https://github.com/astral-sh/ruff)) - An extremely fast Python linter and code formatter.
- Code Formatters
  - <b><code>&nbsp;41438⭐</code></b> <b><code>&nbsp;&nbsp;2746🍴</code></b> [black](https://github.com/psf/black)) - The uncompromising Python code formatter.
  - <b><code>&nbsp;&nbsp;6923⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;622🍴</code></b> [isort](https://github.com/PyCQA/isort)) - A Python utility / library to sort imports.
  - <b><code>&nbsp;46742⭐</code></b> <b><code>&nbsp;&nbsp;1973🍴</code></b> [ruff](https://github.com/astral-sh/ruff)) - An extremely fast Python linter and code formatter.
- Refactoring
  - <b><code>&nbsp;&nbsp;2191⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;179🍴</code></b> [rope](https://github.com/python-rope/rope)) - Rope is a python refactoring library.
- Type Checkers - <b><code>&nbsp;&nbsp;1953⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;76🍴</code></b> [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing))
  - <b><code>&nbsp;20338⭐</code></b> <b><code>&nbsp;&nbsp;3154🍴</code></b> [mypy](https://github.com/python/mypy)) - Check variable types during compile time.
  - <b><code>&nbsp;&nbsp;7149⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;451🍴</code></b> [pyre-check](https://github.com/facebook/pyre-check)) - Performant type checking.
  - <b><code>&nbsp;18095⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;274🍴</code></b> [ty](https://github.com/astral-sh/ty)) - An extremely fast Python type checker and language server.
  - <b><code>&nbsp;&nbsp;5026⭐</code></b> <b><code>&nbsp;&nbsp;1989🍴</code></b> [typeshed](https://github.com/python/typeshed)) - Collection of library stubs for Python, with static types.
- Type Annotations Generators
  - <b><code>&nbsp;&nbsp;4998⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;198🍴</code></b> [monkeytype](https://github.com/Instagram/MonkeyType)) - A system for Python that generates static type annotations by collecting runtime types.
  - <b><code>&nbsp;&nbsp;5031⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;291🍴</code></b> [pytype](https://github.com/google/pytype)) - Pytype checks and infers types for Python code - without requiring type annotations.

## Testing

_Libraries for testing codebases and generating test data._

- Frameworks
  - <b><code>&nbsp;&nbsp;8572⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;640🍴</code></b> [hypothesis](https://github.com/HypothesisWorks/hypothesis)) - Hypothesis is an advanced Quickcheck style property based testing library.
  - <b><code>&nbsp;13707⭐</code></b> <b><code>&nbsp;&nbsp;3067🍴</code></b> [pytest](https://github.com/pytest-dev/pytest)) - A mature full-featured Python testing tool.
  - <b><code>&nbsp;11520⭐</code></b> <b><code>&nbsp;&nbsp;2539🍴</code></b> [robotframework](https://github.com/robotframework/robotframework)) - A generic test automation framework.
  - <b><code>&nbsp;&nbsp;1472⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;94🍴</code></b> [scanapi](https://github.com/scanapi/scanapi)) - Automated Testing and Documentation for your REST API.
  - 🌎 [unittest](docs.python.org/3/library/unittest.html) - (Python standard library) Unit testing framework.
- Test Runners
  - <b><code>&nbsp;&nbsp;1506⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;175🍴</code></b> [nox](https://github.com/wntrblm/nox)) - Flexible test automation for Python.
  - <b><code>&nbsp;&nbsp;3907⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;550🍴</code></b> [tox](https://github.com/tox-dev/tox)) - Auto builds and tests distributions in multiple Python versions
- GUI / Web Testing
  - <b><code>&nbsp;27655⭐</code></b> <b><code>&nbsp;&nbsp;3193🍴</code></b> [locust](https://github.com/locustio/locust)) - Scalable user load testing tool written in Python.
  - <b><code>&nbsp;14453⭐</code></b> <b><code>&nbsp;&nbsp;1135🍴</code></b> [playwright-python](https://github.com/microsoft/playwright-python)) - Python version of the Playwright testing and automation library.
  - <b><code>&nbsp;12397⭐</code></b> <b><code>&nbsp;&nbsp;1408🍴</code></b> [pyautogui](https://github.com/asweigart/pyautogui)) - PyAutoGUI is a cross-platform GUI automation Python module for human beings.
  - <b><code>&nbsp;&nbsp;3168⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;203🍴</code></b> [schemathesis](https://github.com/schemathesis/schemathesis)) - A tool for automatic property-based testing of web applications built with Open API / Swagger specifications.
  - <b><code>&nbsp;34197⭐</code></b> <b><code>&nbsp;&nbsp;8668🍴</code></b> [selenium](https://github.com/SeleniumHQ/selenium)) - Python bindings for 🌎 [Selenium](selenium.dev/) 🌎 [WebDriver](selenium.dev/documentation/webdriver/).
- Mock
  - <b><code>&nbsp;&nbsp;4501⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;292🍴</code></b> [freezegun](https://github.com/spulec/freezegun)) - Travel through time by mocking the datetime module.
  - 🌎 [mock](docs.python.org/3/library/unittest.mock.html) - (Python standard library) A mocking and patching library.
  - <b><code>&nbsp;&nbsp;&nbsp;309⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;49🍴</code></b> [mocket](https://github.com/mindflayer/python-mocket)) - A socket mock framework with gevent/asyncio/SSL support.
  - <b><code>&nbsp;&nbsp;4335⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;362🍴</code></b> [responses](https://github.com/getsentry/responses)) - A utility library for mocking out the requests Python library.
  - <b><code>&nbsp;&nbsp;2955⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;425🍴</code></b> [vcrpy](https://github.com/kevin1024/vcrpy)) - Record and replay HTTP interactions on your tests.
- Object Factories
  - <b><code>&nbsp;&nbsp;3783⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;413🍴</code></b> [factory_boy](https://github.com/FactoryBoy/factory_boy)) - A test fixtures replacement for Python.
  - <b><code>&nbsp;&nbsp;1435⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;110🍴</code></b> [polyfactory](https://github.com/litestar-org/polyfactory)) - mock data generation library with support to classes (continuation of `pydantic-factories`)
- Code Coverage
  - <b><code>&nbsp;&nbsp;3355⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;478🍴</code></b> [coverage](https://github.com/coveragepy/coveragepy)) - Code coverage measurement.
- Fake Data
  - <b><code>&nbsp;19184⭐</code></b> <b><code>&nbsp;&nbsp;2058🍴</code></b> [faker](https://github.com/joke2k/faker)) - A Python package that generates fake data.
  - <b><code>&nbsp;&nbsp;4800⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;358🍴</code></b> [mimesis](https://github.com/lk-geimfari/mimesis)) - is a Python library that help you generate fake data.

## Debugging Tools

_Libraries for debugging code._

- pdb-like Debugger
  - <b><code>&nbsp;&nbsp;1969⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [ipdb](https://github.com/gotcha/ipdb)) - IPython-enabled 🌎 [pdb](docs.python.org/3/library/pdb.html).
  - <b><code>&nbsp;&nbsp;3224⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;240🍴</code></b> [pudb](https://github.com/inducer/pudb)) - A full-screen, console-based Python debugger.
- Tracing
  - <b><code>&nbsp;&nbsp;&nbsp;401⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;25🍴</code></b> [manhole](https://github.com/ionelmc/python-manhole)) - Debugging UNIX socket connections and present the stacktraces for all threads and an interactive prompt.
  - <b><code>&nbsp;&nbsp;&nbsp;863⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51🍴</code></b> [python-hunter](https://github.com/ionelmc/python-hunter)) - A flexible code tracing toolkit.
- Profiler
  - <b><code>&nbsp;15071⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;504🍴</code></b> [py-spy](https://github.com/benfred/py-spy)) - A sampling profiler for Python programs. Written in Rust.
  - <b><code>&nbsp;13335⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;432🍴</code></b> [scalene](https://github.com/plasma-umass/scalene)) - A high-performance, high-precision CPU, GPU, and memory profiler for Python.
- Others
  - <b><code>&nbsp;&nbsp;8351⭐</code></b> <b><code>&nbsp;&nbsp;1078🍴</code></b> [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar)) - Display various debug information for Django.
  - <b><code>&nbsp;&nbsp;&nbsp;979⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;149🍴</code></b> [flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar)) - A port of the django-debug-toolbar to flask.
  - <b><code>&nbsp;10034⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;217🍴</code></b> [icecream](https://github.com/gruns/icecream)) - Inspect variables, expressions, and program execution with a single, simple function call.
  - <b><code>&nbsp;&nbsp;&nbsp;793⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [memory_graph](https://github.com/bterwijn/memory_graph)) - Visualize Python data at runtime to debug references, mutability, and aliasing.

## Build Tools

_Compile software from source code._

- <b><code>&nbsp;&nbsp;&nbsp;511⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;281🍴</code></b> [bitbake](https://github.com/openembedded/bitbake)) - A make-like build tool for embedded Linux.
- <b><code>&nbsp;&nbsp;4723⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;385🍴</code></b> [invoke](https://github.com/pyinvoke/invoke)) - A tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks.
- <b><code>&nbsp;&nbsp;8964⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;854🍴</code></b> [platformio](https://github.com/platformio/platformio-core)) - A console tool to build code with different development platforms.
- <b><code>&nbsp;&nbsp;1965⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;272🍴</code></b> [pybuilder](https://github.com/pybuilder/pybuilder)) - A continuous build tool written in pure Python.
- <b><code>&nbsp;&nbsp;2036⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;187🍴</code></b> [doit](https://github.com/pydoit/doit)) - A task runner and build tool.
- <b><code>&nbsp;&nbsp;2362⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;342🍴</code></b> [scons](https://github.com/SCons/scons)) - A software construction tool.

## Documentation

_Libraries for generating project documentation._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [sphinx](https://github.com/sphinx-doc/sphinx/)) - Python Documentation generator.
  - <b><code>&nbsp;&nbsp;&nbsp;972⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;73🍴</code></b> [awesome-sphinxdoc](https://github.com/ygzgxyz/awesome-sphinxdoc))
- <b><code>&nbsp;42135⭐</code></b> <b><code>&nbsp;&nbsp;2725🍴</code></b> [diagrams](https://github.com/mingrammer/diagrams)) - Diagram as Code.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [mkdocs](https://github.com/mkdocs/mkdocs/)) - Markdown friendly documentation generator.
- <b><code>&nbsp;&nbsp;2481⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;217🍴</code></b> [pdoc](https://github.com/mitmproxy/pdoc)) - Epydoc replacement to auto generate API documentation for Python libraries.

**DevOps**

## DevOps Tools

_Software and libraries for DevOps._

- Cloud Providers
  - <b><code>&nbsp;16852⭐</code></b> <b><code>&nbsp;&nbsp;4507🍴</code></b> [awscli](https://github.com/aws/aws-cli)) - Universal Command Line Interface for Amazon Web Services.
  - <b><code>&nbsp;&nbsp;9749⭐</code></b> <b><code>&nbsp;&nbsp;1964🍴</code></b> [boto3](https://github.com/boto/boto3)) - Python interface to Amazon Web Services.
- Configuration Management
  - <b><code>&nbsp;68381⭐</code></b> <b><code>&nbsp;24165🍴</code></b> [ansible](https://github.com/ansible/ansible)) - A radically simple IT automation platform.
  - <b><code>&nbsp;&nbsp;3639⭐</code></b> <b><code>&nbsp;&nbsp;1053🍴</code></b> [cloudinit](https://github.com/canonical/cloud-init)) - A multi-distribution package that handles early initialization of a cloud instance.
  - <b><code>&nbsp;&nbsp;5866⭐</code></b> <b><code>&nbsp;&nbsp;1620🍴</code></b> [openstack](https://github.com/openstack/openstack)) - Open source software for building private and public clouds.
  - <b><code>&nbsp;&nbsp;4916⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;477🍴</code></b> [pyinfra](https://github.com/pyinfra-dev/pyinfra)) - A versatile CLI tools and python libraries to automate infrastructure.
  - <b><code>&nbsp;15293⭐</code></b> <b><code>&nbsp;&nbsp;5575🍴</code></b> [saltstack](https://github.com/saltstack/salt)) - Infrastructure automation and management system.
- Deployment
  - <b><code>&nbsp;11049⭐</code></b> <b><code>&nbsp;&nbsp;1001🍴</code></b> [chalice](https://github.com/aws/chalice)) - A Python serverless microframework for AWS.
  - <b><code>&nbsp;15409⭐</code></b> <b><code>&nbsp;&nbsp;1960🍴</code></b> [fabric](https://github.com/fabric/fabric)) - A simple, Pythonic tool for remote execution and deployment.
- Monitoring and Processes
  - <b><code>&nbsp;11125⭐</code></b> <b><code>&nbsp;&nbsp;1466🍴</code></b> [psutil](https://github.com/giampaolo/psutil)) - A cross-platform process and system utilities module.
  - <b><code>&nbsp;&nbsp;2159⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;601🍴</code></b> [sentry-python](https://github.com/getsentry/sentry-python)) - Sentry SDK for Python.
  - <b><code>&nbsp;&nbsp;7246⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;504🍴</code></b> [sh](https://github.com/amoffat/sh)) - A full-fledged subprocess replacement for Python.
  - <b><code>&nbsp;&nbsp;9017⭐</code></b> <b><code>&nbsp;&nbsp;1265🍴</code></b> [supervisor](https://github.com/Supervisor/supervisor)) - Supervisor process control system for UNIX.
- Other
  - <b><code>&nbsp;13132⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;837🍴</code></b> [borg](https://github.com/borgbackup/borg)) - A deduplicating archiver with compression and encryption.
  - <b><code>&nbsp;&nbsp;2005⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;201🍴</code></b> [chaostoolkit](https://github.com/chaostoolkit/chaostoolkit)) - A Chaos Engineering toolkit & Orchestration for Developers.
  - <b><code>&nbsp;15091⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;941🍴</code></b> [pre-commit](https://github.com/pre-commit/pre-commit)) - A framework for managing and maintaining multi-language pre-commit hooks.

## Distributed Computing

_Frameworks and libraries for Distributed Computing._

- Batch Processing
  - <b><code>&nbsp;13779⭐</code></b> <b><code>&nbsp;&nbsp;1858🍴</code></b> [dask](https://github.com/dask/dask)) - A flexible parallel computing library for analytic computing.
  - <b><code>&nbsp;18708⭐</code></b> <b><code>&nbsp;&nbsp;2453🍴</code></b> [luigi](https://github.com/spotify/luigi)) - A module that helps you build complex pipelines of batch jobs.
  - <b><code>&nbsp;&nbsp;&nbsp;904⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;132🍴</code></b> [mpi4py](https://github.com/mpi4py/mpi4py)) - Python bindings for MPI.
  - <b><code>&nbsp;43056⭐</code></b> <b><code>&nbsp;29140🍴</code></b> [pyspark](https://github.com/apache/spark)) - 🌎 [Apache Spark](spark.apache.org/) Python API.
  - <b><code>&nbsp;&nbsp;4332⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;450🍴</code></b> [joblib](https://github.com/joblib/joblib)) - A set of tools to provide lightweight pipelining in Python.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [ray](https://github.com/ray-project/ray/)) - A system for parallel and distributed Python that unifies the machine learning ecosystem.

## Task Queues

_Libraries for working with task queues._

- <b><code>&nbsp;28266⭐</code></b> <b><code>&nbsp;&nbsp;4997🍴</code></b> [celery](https://github.com/celery/celery)) - An asynchronous task queue/job queue based on distributed message passing.
- <b><code>&nbsp;&nbsp;5188⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;357🍴</code></b> [dramatiq](https://github.com/Bogdanp/dramatiq)) - A fast and reliable background task processing library for Python 3.
- <b><code>&nbsp;&nbsp;5943⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;393🍴</code></b> [huey](https://github.com/coleifer/huey)) - Little multi-threaded task queue.
- <b><code>&nbsp;10615⭐</code></b> <b><code>&nbsp;&nbsp;1463🍴</code></b> [rq](https://github.com/rq/rq)) - Simple job queues for Python.

## Job Schedulers

_Libraries for scheduling jobs._

- <b><code>&nbsp;44819⭐</code></b> <b><code>&nbsp;16785🍴</code></b> [airflow](https://github.com/apache/airflow)) - Airflow is a platform to programmatically author, schedule and monitor workflows.
- <b><code>&nbsp;&nbsp;7391⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;751🍴</code></b> [apscheduler](https://github.com/agronholm/apscheduler)) - A light but powerful in-process task scheduler that lets you schedule functions.
- <b><code>&nbsp;15160⭐</code></b> <b><code>&nbsp;&nbsp;2039🍴</code></b> [dagster](https://github.com/dagster-io/dagster)) - An orchestration platform for the development, production, and observation of data assets.
- <b><code>&nbsp;21984⭐</code></b> <b><code>&nbsp;&nbsp;2190🍴</code></b> [prefect](https://github.com/PrefectHQ/prefect)) - A modern workflow orchestration framework that makes it easy to build, schedule and monitor robust data pipelines.
- <b><code>&nbsp;12244⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;993🍴</code></b> [schedule](https://github.com/dbader/schedule)) - Python job scheduling for humans.
- <b><code>&nbsp;&nbsp;1871⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;338🍴</code></b> [SpiffWorkflow](https://github.com/sartography/SpiffWorkflow)) - A powerful workflow engine implemented in pure Python.

## Logging

_Libraries for generating and working with logs._

- <b><code>&nbsp;&nbsp;&nbsp;102⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;11🍴</code></b> [logfmter](https://github.com/josheppinette/python-logfmter)) - A standard library compatible logfmt formatter.
- 🌎 [logging](docs.python.org/3/library/logging.html) - (Python standard library) Logging facility for Python.
- <b><code>&nbsp;23750⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;777🍴</code></b> [loguru](https://github.com/Delgan/loguru)) - Library which aims to bring enjoyable logging in Python.
- <b><code>&nbsp;&nbsp;4676⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;273🍴</code></b> [structlog](https://github.com/hynek/structlog)) - Structured logging made easy.

## Network Virtualization

_Tools and libraries for Virtual Networking and SDN (Software Defined Networking)._

- <b><code>&nbsp;&nbsp;5793⭐</code></b> <b><code>&nbsp;&nbsp;1795🍴</code></b> [mininet](https://github.com/mininet/mininet)) - A popular network emulator and API written in Python.
- <b><code>&nbsp;&nbsp;2443⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;581🍴</code></b> [napalm](https://github.com/napalm-automation/napalm)) - Cross-vendor API to manipulate network devices.
- <b><code>&nbsp;12143⭐</code></b> <b><code>&nbsp;&nbsp;2200🍴</code></b> [scapy](https://github.com/secdev/scapy)) - A brilliant packet manipulation library.

**CLI & GUI**

## CLI Development

_Libraries for building command-line applications._

- CLI Development
  - 🌎 [argparse](docs.python.org/3/library/argparse.html) - (Python standard library) Command-line option and argument parsing.
  - <b><code>&nbsp;&nbsp;1343⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;117🍴</code></b> [cement](https://github.com/datafolklabs/cement)) - CLI Application Framework for Python.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [click](https://github.com/pallets/click/)) - A package for creating beautiful command line interfaces in a composable way.
  - <b><code>&nbsp;28159⭐</code></b> <b><code>&nbsp;&nbsp;1475🍴</code></b> [python-fire](https://github.com/google/python-fire)) - A library for creating command line interfaces from absolutely any Python object.
  - <b><code>&nbsp;10348⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;774🍴</code></b> [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)) - A library for building powerful interactive command lines.
  - <b><code>&nbsp;19096⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;862🍴</code></b> [typer](https://github.com/fastapi/typer)) - Modern CLI framework that uses Python type hints. Built on Click and Pydantic.
- Terminal Rendering
  - <b><code>&nbsp;&nbsp;6259⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;232🍴</code></b> [alive-progress](https://github.com/rsalmei/alive-progress)) - A new kind of Progress Bar, with real-time throughput, eta and very cool animations.
  - <b><code>&nbsp;&nbsp;4273⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;261🍴</code></b> [asciimatics](https://github.com/peterbrittain/asciimatics)) - A package to create full-screen text UIs (from interactive forms to ASCII animations).
  - <b><code>&nbsp;&nbsp;3774⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;270🍴</code></b> [colorama](https://github.com/tartley/colorama)) - Cross-platform colored terminal text.
  - <b><code>&nbsp;55913⭐</code></b> <b><code>&nbsp;&nbsp;2080🍴</code></b> [rich](https://github.com/Textualize/rich)) - Python library for rich text and beautiful formatting in the terminal. Also provides a great `RichHandler` log handler.
  - <b><code>&nbsp;35102⭐</code></b> <b><code>&nbsp;&nbsp;1148🍴</code></b> [textual](https://github.com/Textualize/textual)) - A framework for building interactive user interfaces that run in the terminal and the browser.
  - <b><code>&nbsp;31068⭐</code></b> <b><code>&nbsp;&nbsp;1442🍴</code></b> [tqdm](https://github.com/tqdm/tqdm)) - Fast, extensible progress bar for loops and CLI.

## CLI Tools

_Useful CLI-based tools for productivity._

- Productivity Tools
  - <b><code>&nbsp;24777⭐</code></b> <b><code>&nbsp;&nbsp;2215🍴</code></b> [cookiecutter](https://github.com/cookiecutter/cookiecutter)) - A command-line utility that creates projects from cookiecutters (project templates).
  - <b><code>&nbsp;&nbsp;3240⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;248🍴</code></b> [copier](https://github.com/copier-org/copier)) - A library and command-line utility for rendering projects templates.
  - <b><code>&nbsp;&nbsp;3565⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;100🍴</code></b> [doitlive](https://github.com/sloria/doitlive)) - A tool for live presentations in the terminal.
  - <b><code>&nbsp;95769⭐</code></b> <b><code>&nbsp;&nbsp;3863🍴</code></b> [thefuck](https://github.com/nvbn/thefuck)) - Correcting your previous console command.
  - <b><code>&nbsp;&nbsp;4462⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;236🍴</code></b> [tmuxp](https://github.com/tmux-python/tmuxp)) - A <b><code>&nbsp;43706⭐</code></b> <b><code>&nbsp;&nbsp;2524🍴</code></b> [tmux](https://github.com/tmux/tmux)) session manager.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [xonsh](https://github.com/xonsh/xonsh/)) - A Python-powered shell. Full-featured and cross-platform.
  - <b><code>153869⭐</code></b> <b><code>&nbsp;12486🍴</code></b> [yt-dlp](https://github.com/yt-dlp/yt-dlp)) - A command-line program to download videos from YouTube and other video sites, a fork of youtube-dl.
- CLI Enhancements
  - <b><code>&nbsp;37787⭐</code></b> <b><code>&nbsp;&nbsp;3845🍴</code></b> [httpie](https://github.com/httpie/cli)) - A command line HTTP client, a user-friendly cURL replacement.
  - <b><code>&nbsp;&nbsp;2724⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;116🍴</code></b> [iredis](https://github.com/laixintao/iredis)) - Redis CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;&nbsp;3220⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;93🍴</code></b> [litecli](https://github.com/dbcli/litecli)) - SQLite CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;11892⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;686🍴</code></b> [mycli](https://github.com/dbcli/mycli)) - MySQL CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;13086⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;584🍴</code></b> [pgcli](https://github.com/dbcli/pgcli)) - PostgreSQL CLI with autocompletion and syntax highlighting.

## GUI Development

_Libraries for working with graphical user interface applications._

- Desktop
  - <b><code>&nbsp;13242⭐</code></b> <b><code>&nbsp;&nbsp;1153🍴</code></b> [customtkinter](https://github.com/tomschimansky/customtkinter)) - A modern and customizable python UI-library based on Tkinter.
  - <b><code>&nbsp;15312⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;778🍴</code></b> [dearpygui](https://github.com/hoffstadt/DearPyGui)) - A Simple GPU accelerated Python GUI framework
  - <b><code>&nbsp;&nbsp;1576⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;132🍴</code></b> [enaml](https://github.com/nucleic/enaml)) - Creating beautiful user-interfaces with Declarative Syntax like QML.
  - <b><code>&nbsp;18910⭐</code></b> <b><code>&nbsp;&nbsp;3157🍴</code></b> [kivy](https://github.com/kivy/kivy)) - A library for creating NUI applications, running on Windows, Linux, Mac OS X, Android and iOS.
  - <b><code>&nbsp;&nbsp;2179⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;330🍴</code></b> [pyglet](https://github.com/pyglet/pyglet)) - A cross-platform windowing and multimedia library for Python.
  - <b><code>&nbsp;&nbsp;&nbsp;156⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30🍴</code></b> [pygobject](https://github.com/GNOME/pygobject)) - Python Bindings for GLib/GObject/GIO/GTK+ (GTK+3).
  - 🌎 [PyQt](www.riverbankcomputing.com/static/Docs/PyQt6/) - Python bindings for the 🌎 [Qt](www.qt.io/) cross-platform application and UI framework.
  - <b><code>&nbsp;&nbsp;&nbsp;119⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;25🍴</code></b> [pyside](https://github.com/pyside/pyside-setup)) - Qt for Python offers the official Python bindings for 🌎 [Qt](www.qt.io/), this is same as PyQt but it's the official binding with different licensing.
  - 🌎 [tkinter](docs.python.org/3/library/tkinter.html) - (Python standard library) The standard Python interface to the Tcl/Tk GUI toolkit.
  - <b><code>&nbsp;&nbsp;5327⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;796🍴</code></b> [toga](https://github.com/beeware/toga)) - A Python native, OS native GUI toolkit.
  - <b><code>&nbsp;&nbsp;2596⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;558🍴</code></b> [wxPython](https://github.com/wxWidgets/Phoenix)) - A blending of the wxWidgets C++ class library with the Python.
- Web-based
  - <b><code>&nbsp;15814⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;641🍴</code></b> [flet](https://github.com/flet-dev/flet)) - Cross-platform GUI framework for building modern apps in pure Python.
  - <b><code>&nbsp;15572⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;909🍴</code></b> [nicegui](https://github.com/zauberzeug/nicegui)) - An easy-to-use, Python-based UI framework, which shows up in your web browser.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [pywebview](https://github.com/r0x0r/pywebview/)) - A lightweight cross-platform native wrapper around a webview component.
- Terminal
  - 🌎 [curses](docs.python.org/3/library/curses.html) - Built-in wrapper for [ncurses](http://www.gnu.org/software/ncurses/) used to create terminal GUI applications.
  - <b><code>&nbsp;&nbsp;2996⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;331🍴</code></b> [urwid](https://github.com/urwid/urwid)) - A library for creating terminal GUI applications with strong support for widgets, events, rich colors, etc.
- Wrappers
  - <b><code>&nbsp;22030⭐</code></b> <b><code>&nbsp;&nbsp;1043🍴</code></b> [gooey](https://github.com/chriskiehl/Gooey)) - Turn command line programs into a full GUI application with one line.

**Text & Documents**

## Text Processing

_Libraries for parsing and manipulating plain texts._

- General
  - <b><code>&nbsp;&nbsp;1435⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;469🍴</code></b> [babel](https://github.com/python-babel/babel)) - An internationalization library for Python.
  - <b><code>&nbsp;&nbsp;2538⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;290🍴</code></b> [chardet](https://github.com/chardet/chardet)) - Python 2/3 compatible character encoding detector.
  - 🌎 [difflib](docs.python.org/3/library/difflib.html) - (Python standard library) Helpers for computing deltas.
  - <b><code>&nbsp;&nbsp;4017⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;125🍴</code></b> [ftfy](https://github.com/rspeer/python-ftfy)) - Makes Unicode text less broken and more consistent automagically.
  - <b><code>&nbsp;&nbsp;&nbsp;277⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;25🍴</code></b> [pangu.py](https://github.com/vinta/pangu.py)) - Paranoid text spacing.
  - <b><code>&nbsp;&nbsp;1553⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;152🍴</code></b> [pyfiglet](https://github.com/pwaller/pyfiglet)) - An implementation of figlet written in Python.
  - <b><code>&nbsp;&nbsp;5275⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;629🍴</code></b> [pypinyin](https://github.com/mozillazg/python-pinyin)) - Convert Chinese hanzi (漢字) to pinyin (拼音).
  - <b><code>&nbsp;&nbsp;1601⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;116🍴</code></b> [python-slugify](https://github.com/un33k/python-slugify)) - A Python slugify library that translates unicode to ASCII.
  - <b><code>&nbsp;&nbsp;3527⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;256🍴</code></b> [textdistance](https://github.com/life4/textdistance)) - Compute distance between sequences with 30+ algorithms.
  - <b><code>&nbsp;&nbsp;&nbsp;604⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;68🍴</code></b> [unidecode](https://github.com/avian2/unidecode)) - ASCII transliterations of Unicode text.
- Unique identifiers
  - <b><code>&nbsp;&nbsp;&nbsp;496⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [sqids](https://github.com/sqids/sqids-python)) - A library for generating short unique IDs from numbers.
  - <b><code>&nbsp;&nbsp;2181⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;117🍴</code></b> [shortuuid](https://github.com/skorokithakis/shortuuid)) - A generator library for concise, unambiguous and URL-safe UUIDs.
- Parser
  - <b><code>&nbsp;&nbsp;2135⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;785🍴</code></b> [pygments](https://github.com/pygments/pygments)) - A generic syntax highlighter.
  - <b><code>&nbsp;&nbsp;2465⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;307🍴</code></b> [pyparsing](https://github.com/pyparsing/pyparsing)) - A general purpose framework for generating parsers.
  - <b><code>&nbsp;&nbsp;&nbsp;704⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;106🍴</code></b> [python-nameparser](https://github.com/derek73/python-nameparser)) - Parsing human names into their individual components.
  - <b><code>&nbsp;&nbsp;3723⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;440🍴</code></b> [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)) - Parsing, formatting, storing and validating international phone numbers.
  - <b><code>&nbsp;&nbsp;1519⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;195🍴</code></b> [python-user-agents](https://github.com/selwin/python-user-agents)) - Browser user agent parser.
  - <b><code>&nbsp;&nbsp;4002⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;721🍴</code></b> [sqlparse](https://github.com/andialbrecht/sqlparse)) - A non-validating SQL parser.

## HTML Manipulation

_Libraries for working with HTML and XML._

- 🌎 [beautifulsoup](www.crummy.com/software/BeautifulSoup/bs4/doc/) - Providing Pythonic idioms for iterating, searching, and modifying HTML or XML.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [justhtml](https://github.com/EmilStenstrom/justhtml/)) - A pure Python HTML5 parser that just works.
- <b><code>&nbsp;&nbsp;3004⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;612🍴</code></b> [lxml](https://github.com/lxml/lxml)) - A very fast, easy-to-use and versatile library for handling HTML and XML.
- <b><code>&nbsp;&nbsp;&nbsp;685⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;174🍴</code></b> [markupsafe](https://github.com/pallets/markupsafe)) - Implements a XML/HTML/XHTML Markup safe string for Python.
- <b><code>&nbsp;&nbsp;2379⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;185🍴</code></b> [pyquery](https://github.com/gawel/pyquery)) - A jQuery-like library for parsing HTML.
- <b><code>&nbsp;&nbsp;&nbsp;184⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;25🍴</code></b> [tinycss2](https://github.com/Kozea/tinycss2)) - A low-level CSS parser and generator written in Python.
- <b><code>&nbsp;&nbsp;5728⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;469🍴</code></b> [xmltodict](https://github.com/martinblech/xmltodict)) - Working with XML feel like you are working with JSON.

## File Format Processing

_Libraries for parsing and manipulating specific text formats._

- General
  - <b><code>&nbsp;56717⭐</code></b> <b><code>&nbsp;&nbsp;3850🍴</code></b> [docling](https://github.com/docling-project/docling)) - Library for converting documents into structured data.
  - <b><code>&nbsp;&nbsp;7161⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;344🍴</code></b> [kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)) - High-performance document extraction library with a Rust core, supporting 62+ formats including PDF, Office, images with OCR, HTML, email, and archives.
  - <b><code>&nbsp;&nbsp;2223⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;536🍴</code></b> [pyelftools](https://github.com/eliben/pyelftools)) - Parsing and analyzing ELF files and DWARF debugging information.
  - <b><code>&nbsp;&nbsp;4752⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;593🍴</code></b> [tablib](https://github.com/jazzband/tablib)) - A module for Tabular Datasets in XLS, CSV, JSON, YAML.
- MS Office
  - <b><code>&nbsp;&nbsp;2595⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;431🍴</code></b> [docxtpl](https://github.com/elapouya/python-docx-template)) - Editing a docx document by jinja2 template
  - 🌎 [openpyxl](openpyxl.readthedocs.io/en/stable/) - A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.
  - <b><code>&nbsp;&nbsp;1284⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;167🍴</code></b> [pyexcel](https://github.com/pyexcel/pyexcel)) - Providing one API for reading, manipulating and writing csv, ods, xls, xlsx and xlsm files.
  - <b><code>&nbsp;&nbsp;5505⭐</code></b> <b><code>&nbsp;&nbsp;1266🍴</code></b> [python-docx](https://github.com/python-openxml/python-docx)) - Reads, queries and modifies Microsoft Word 2007/2008 docx files.
  - <b><code>&nbsp;&nbsp;3256⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;682🍴</code></b> [python-pptx](https://github.com/scanny/python-pptx)) - Python library for creating and updating PowerPoint (.pptx) files.
  - <b><code>&nbsp;&nbsp;3918⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;661🍴</code></b> [xlsxwriter](https://github.com/jmcnamara/XlsxWriter)) - A Python module for creating Excel .xlsx files.
  - <b><code>&nbsp;&nbsp;3326⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;529🍴</code></b> [xlwings](https://github.com/xlwings/xlwings)) - A BSD-licensed library that makes it easy to call Python from Excel and vice versa.
- PDF
  - <b><code>&nbsp;&nbsp;&nbsp;521⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;60🍴</code></b> [pdf_oxide](https://github.com/yfedoseev/pdf_oxide)) - A fast PDF library for text extraction, image extraction, and markdown conversion, powered by Rust.
  - <b><code>&nbsp;&nbsp;6940⭐</code></b> <b><code>&nbsp;&nbsp;1024🍴</code></b> [pdfminer.six](https://github.com/pdfminer/pdfminer.six)) - Pdfminer.six is a community maintained fork of the original PDFMiner.
  - <b><code>&nbsp;&nbsp;2677⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;222🍴</code></b> [pikepdf](https://github.com/pikepdf/pikepdf)) - A powerful library for reading and editing PDF files, based on qpdf.
  - <b><code>&nbsp;&nbsp;9903⭐</code></b> <b><code>&nbsp;&nbsp;1556🍴</code></b> [pypdf](https://github.com/py-pdf/pypdf)) - A library capable of splitting, merging, cropping, and transforming PDF pages.
  - 🌎 [reportlab](www.reportlab.com/opensource/) - Allowing Rapid creation of rich PDF documents.
  - <b><code>&nbsp;&nbsp;8781⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;795🍴</code></b> [weasyprint](https://github.com/Kozea/WeasyPrint)) - A visual rendering engine for HTML and CSS that can export to PDF.
- Markdown
  - <b><code>&nbsp;&nbsp;1266⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;94🍴</code></b> [markdown-it-py](https://github.com/executablebooks/markdown-it-py)) - Markdown parser with 100% CommonMark support, extensions, and syntax plugins.
  - <b><code>&nbsp;&nbsp;4192⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;896🍴</code></b> [markdown](https://github.com/waylan/Python-Markdown)) - A Python implementation of John Gruber’s Markdown.
  - <b><code>&nbsp;92826⭐</code></b> <b><code>&nbsp;&nbsp;5587🍴</code></b> [markitdown](https://github.com/microsoft/markitdown)) - Python tool for converting files and office documents to Markdown.
  - <b><code>&nbsp;&nbsp;3006⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;278🍴</code></b> [mistune](https://github.com/lepture/mistune)) - Fastest and full featured pure Python parsers of Markdown.
- Data Formats
  - <b><code>&nbsp;&nbsp;6360⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;674🍴</code></b> [csvkit](https://github.com/wireservice/csvkit)) - Utilities for converting to and working with CSV.
  - <b><code>&nbsp;&nbsp;2871⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;575🍴</code></b> [pyyaml](https://github.com/yaml/pyyaml)) - YAML implementations for Python.
  - 🌎 [tomllib](docs.python.org/3/library/tomllib.html) - (Python standard library) Parse TOML files.

## File Manipulation

_Libraries for file manipulation._

- 🌎 [mimetypes](docs.python.org/3/library/mimetypes.html) - (Python standard library) Map filenames to MIME types.
- 🌎 [pathlib](docs.python.org/3/library/pathlib.html) - (Python standard library) A cross-platform, object-oriented path library.
- <b><code>&nbsp;&nbsp;2900⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;306🍴</code></b> [python-magic](https://github.com/ahupp/python-magic)) - A Python interface to the libmagic file type identification library.
- <b><code>&nbsp;&nbsp;7296⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;747🍴</code></b> [watchdog](https://github.com/gorakhargosh/watchdog)) - API and shell utilities to monitor file system events.
- <b><code>&nbsp;&nbsp;2454⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;133🍴</code></b> [watchfiles](https://github.com/samuelcolvin/watchfiles)) - Simple, modern and fast file watching and code reload in python.

**Media**

## Image Processing

_Libraries for manipulating images._

- <b><code>&nbsp;13474⭐</code></b> <b><code>&nbsp;&nbsp;2410🍴</code></b> [pillow](https://github.com/python-pillow/Pillow)) - Pillow is the friendly 🌎 [PIL](www.pythonware.com/products/pil/) fork.
- <b><code>&nbsp;&nbsp;1892⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;226🍴</code></b> [pymatting](https://github.com/pymatting/pymatting)) - A library for alpha matting.
- <b><code>&nbsp;&nbsp;&nbsp;651⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;133🍴</code></b> [python-barcode](https://github.com/WhyNotHugo/python-barcode)) - Create barcodes in Python with no extra dependencies.
- <b><code>&nbsp;&nbsp;4873⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;727🍴</code></b> [python-qrcode](https://github.com/lincolnloop/python-qrcode)) - A pure Python QR Code generator.
- <b><code>&nbsp;&nbsp;&nbsp;791⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;56🍴</code></b> [pyvips](https://github.com/libvips/pyvips)) - A fast image processing library with low memory needs.
- <b><code>&nbsp;&nbsp;6487⭐</code></b> <b><code>&nbsp;&nbsp;2368🍴</code></b> [scikit-image](https://github.com/scikit-image/scikit-image)) - A Python library for (scientific) image processing.
- <b><code>&nbsp;10469⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;862🍴</code></b> [thumbor](https://github.com/thumbor/thumbor)) - A smart imaging service. It enables on-demand crop, re-sizing and flipping of images.
- <b><code>&nbsp;&nbsp;1481⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;198🍴</code></b> [wand](https://github.com/emcconville/wand)) - Python bindings for 🌎 [MagickWand](www.imagemagick.org/script/magick-wand.php), C API for ImageMagick.

## Audio & Video Processing

_Libraries for manipulating audio, video, and their metadata._

- Audio
  - <b><code>&nbsp;&nbsp;2599⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;383🍴</code></b> [gtts](https://github.com/pndurette/gTTS)) - Python library and CLI tool for converting text to speech using Google Translate TTS.
  - <b><code>&nbsp;&nbsp;8291⭐</code></b> <b><code>&nbsp;&nbsp;1042🍴</code></b> [librosa](https://github.com/librosa/librosa)) - Python library for audio and music analysis.
  - <b><code>&nbsp;&nbsp;2457⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;260🍴</code></b> [matchering](https://github.com/sergree/matchering)) - A library for automated reference audio mastering.
  - <b><code>&nbsp;&nbsp;9746⭐</code></b> <b><code>&nbsp;&nbsp;1121🍴</code></b> [pydub](https://github.com/jiaaro/pydub)) - Manipulate audio with a simple and easy high level interface.
- Video
  - <b><code>&nbsp;14486⭐</code></b> <b><code>&nbsp;&nbsp;2042🍴</code></b> [moviepy](https://github.com/Zulko/moviepy)) - A module for script-based movie editing with many formats, including animated GIFs.
  - <b><code>&nbsp;&nbsp;3689⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;279🍴</code></b> [vidgear](https://github.com/abhiTronix/vidgear)) - Most Powerful multi-threaded Video Processing framework.
- Metadata
  - <b><code>&nbsp;14899⭐</code></b> <b><code>&nbsp;&nbsp;1997🍴</code></b> [beets](https://github.com/beetbox/beets)) - A music library manager and 🌎 [MusicBrainz](musicbrainz.org/) tagger.
  - <b><code>&nbsp;&nbsp;1878⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;187🍴</code></b> [mutagen](https://github.com/quodlibet/mutagen)) - A Python module to handle audio metadata.
  - <b><code>&nbsp;&nbsp;&nbsp;807⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;104🍴</code></b> [tinytag](https://github.com/devsnd/tinytag)) - A library for reading music meta data of MP3, OGG, FLAC and Wave files.

## Game Development

_Awesome game development libraries._

- <b><code>&nbsp;&nbsp;2007⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;366🍴</code></b> [arcade](https://github.com/pythonarcade/arcade)) - Arcade is a modern Python framework for crafting games with compelling graphics and sound.
- <b><code>&nbsp;&nbsp;5079⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;869🍴</code></b> [panda3d](https://github.com/panda3d/panda3d)) - 3D game engine developed by Disney.
- <b><code>&nbsp;&nbsp;&nbsp;338⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;52🍴</code></b> [py-sdl2](https://github.com/py-sdl/py-sdl2)) - A ctypes based wrapper for the SDL2 library.
- <b><code>&nbsp;&nbsp;8690⭐</code></b> <b><code>&nbsp;&nbsp;4067🍴</code></b> [pygame](https://github.com/pygame/pygame)) - Pygame is a set of Python modules designed for writing games.
- <b><code>&nbsp;&nbsp;&nbsp;399⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;126🍴</code></b> [pyopengl](https://github.com/mcfletch/pyopengl)) - Python ctypes bindings for OpenGL and it's related APIs.
- <b><code>&nbsp;&nbsp;6341⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;868🍴</code></b> [renpy](https://github.com/renpy/renpy)) - A Visual Novel engine.

**Python Language**

## Implementations

_Implementations of Python._

- <b><code>&nbsp;72116⭐</code></b> <b><code>&nbsp;34329🍴</code></b> [cpython](https://github.com/python/cpython)) - Default, most widely used implementation of the Python programming language written in C.
- <b><code>&nbsp;10669⭐</code></b> <b><code>&nbsp;&nbsp;1611🍴</code></b> [cython](https://github.com/cython/cython)) - Optimizing Static Compiler for Python.
- <b><code>&nbsp;&nbsp;2738⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;312🍴</code></b> [ironpython](https://github.com/IronLanguages/ironpython3)) - Implementation of the Python programming language written in C#.
- <b><code>&nbsp;21588⭐</code></b> <b><code>&nbsp;&nbsp;8763🍴</code></b> [micropython](https://github.com/micropython/micropython)) - A lean and efficient Python programming language implementation.
- <b><code>&nbsp;14480⭐</code></b> <b><code>&nbsp;&nbsp;1003🍴</code></b> [pyodide](https://github.com/pyodide/pyodide)) - Python distribution for the browser and Node.js based on WebAssembly.
- <b><code>&nbsp;&nbsp;1694⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;109🍴</code></b> [pypy](https://github.com/pypy/pypy)) - A very fast and compliant implementation of the Python language.

## Built-in Classes Enhancement

_Libraries for enhancing Python built-in classes._

- <b><code>&nbsp;&nbsp;5755⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;424🍴</code></b> [attrs](https://github.com/python-attrs/attrs)) - Replacement for `__init__`, `__eq__`, `__repr__`, etc. boilerplate in class definitions.
- <b><code>&nbsp;&nbsp;1579⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;64🍴</code></b> [bidict](https://github.com/jab/bidict)) - Efficient, Pythonic bidirectional map data structures and related functionality.
- <b><code>&nbsp;&nbsp;2823⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [box](https://github.com/cdgriffith/Box)) - Python dictionaries with advanced dot notation access.

## Functional Programming

_Functional Programming with Python._

- <b><code>&nbsp;&nbsp;4316⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;140🍴</code></b> [coconut](https://github.com/evhub/coconut)) - A variant of Python built for simple, elegant, Pythonic functional programming.
- 🌎 [functools](docs.python.org/3/library/functools.html) - (Python standard library) Higher-order functions and operations on callable objects.
- <b><code>&nbsp;&nbsp;3500⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [funcy](https://github.com/Suor/funcy)) - A fancy and practical functional tools.
- <b><code>&nbsp;&nbsp;4048⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;311🍴</code></b> [more-itertools](https://github.com/erikrose/more-itertools)) - More routines for operating on iterables, beyond `itertools`.
- <b><code>&nbsp;&nbsp;4245⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;144🍴</code></b> [returns](https://github.com/dry-python/returns)) - A set of type-safe monads, transformers, and composition utilities.
- <b><code>&nbsp;&nbsp;5134⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;271🍴</code></b> [toolz](https://github.com/pytoolz/toolz)) - A collection of functional utilities for iterators, functions, and dictionaries. Also available as <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [cytoolz](https://github.com/pytoolz/cytoolz/)) for Cython-accelerated performance.

## Asynchronous Programming

_Libraries for asynchronous, concurrent and parallel execution. Also see <b><code>&nbsp;&nbsp;5034⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;346🍴</code></b> [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio))._

- <b><code>&nbsp;&nbsp;2424⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;189🍴</code></b> [anyio](https://github.com/agronholm/anyio)) - A high-level async concurrency and networking framework that works on top of asyncio or trio.
- 🌎 [asyncio](docs.python.org/3/library/asyncio.html) - (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
  - <b><code>&nbsp;&nbsp;5034⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;346🍴</code></b> [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio))
- 🌎 [concurrent.futures](docs.python.org/3/library/concurrent.futures.html) - (Python standard library) A high-level interface for asynchronously executing callables.
- <b><code>&nbsp;&nbsp;6448⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;963🍴</code></b> [gevent](https://github.com/gevent/gevent)) - A coroutine-based Python networking library that uses <b><code>&nbsp;&nbsp;1815⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;266🍴</code></b> [greenlet](https://github.com/python-greenlet/greenlet)).
- 🌎 [multiprocessing](docs.python.org/3/library/multiprocessing.html) - (Python standard library) Process-based parallelism.
- <b><code>&nbsp;&nbsp;7219⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;394🍴</code></b> [trio](https://github.com/python-trio/trio)) - A friendly library for async concurrency and I/O.
- <b><code>&nbsp;&nbsp;5956⭐</code></b> <b><code>&nbsp;&nbsp;1208🍴</code></b> [twisted](https://github.com/twisted/twisted)) - An event-driven networking engine.
- <b><code>&nbsp;11729⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;607🍴</code></b> [uvloop](https://github.com/MagicStack/uvloop)) - Ultra fast asyncio event loop.

## Date and Time

_Libraries for working with dates and times._

- <b><code>&nbsp;&nbsp;2797⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;489🍴</code></b> [dateparser](https://github.com/scrapinghub/dateparser)) - A Python parser for human-readable dates in dozens of languages.
- <b><code>&nbsp;&nbsp;2606⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;537🍴</code></b> [dateutil](https://github.com/dateutil/dateutil)) - Extensions to the standard Python 🌎 [datetime](docs.python.org/3/library/datetime.html) module.
- <b><code>&nbsp;&nbsp;6632⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;423🍴</code></b> [pendulum](https://github.com/python-pendulum/pendulum)) - Python datetimes made easy.
- 🌎 [zoneinfo](docs.python.org/3/library/zoneinfo.html) - (Python standard library) IANA time zone support. Brings the 🌎 [tz database](en.wikipedia.org/wiki/Tz_database) into Python.

**Python Toolchain**

## Environment Management

_Libraries for Python version and virtual environment management._

- <b><code>&nbsp;44509⭐</code></b> <b><code>&nbsp;&nbsp;3242🍴</code></b> [pyenv](https://github.com/pyenv/pyenv)) - Simple Python version management.
- <b><code>&nbsp;&nbsp;7107⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;570🍴</code></b> [pyenv-win](https://github.com/pyenv-win/pyenv-win)) - Pyenv for Windows.
- <b><code>&nbsp;82256⭐</code></b> <b><code>&nbsp;&nbsp;2876🍴</code></b> [uv](https://github.com/astral-sh/uv)) - An extremely fast Python version, package and project manager, written in Rust.
- <b><code>&nbsp;&nbsp;5020⭐</code></b> <b><code>&nbsp;&nbsp;1089🍴</code></b> [virtualenv](https://github.com/pypa/virtualenv)) - A tool to create isolated Python environments.

## Package Management

_Libraries for package and dependency management._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [conda](https://github.com/conda/conda/)) - Cross-platform, Python-agnostic binary package manager.
- <b><code>&nbsp;10147⭐</code></b> <b><code>&nbsp;&nbsp;3253🍴</code></b> [pip](https://github.com/pypa/pip)) - The package installer for Python.
- <b><code>&nbsp;12660⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;535🍴</code></b> [pipx](https://github.com/pypa/pipx)) - Install and Run Python Applications in Isolated Environments. Like `npx` in Node.js.
- <b><code>&nbsp;34268⭐</code></b> <b><code>&nbsp;&nbsp;2421🍴</code></b> [poetry](https://github.com/python-poetry/poetry)) - Python dependency management and packaging made easy.
- <b><code>&nbsp;82256⭐</code></b> <b><code>&nbsp;&nbsp;2876🍴</code></b> [uv](https://github.com/astral-sh/uv)) - An extremely fast Python version, package and project manager, written in Rust.

## Package Repositories

_Local PyPI repository server and proxies._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [bandersnatch](https://github.com/pypa/bandersnatch/)) - PyPI mirroring tool provided by Python Packaging Authority (PyPA).
- <b><code>&nbsp;&nbsp;1150⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;142🍴</code></b> [devpi](https://github.com/devpi/devpi)) - PyPI server and packaging/testing/release tool.
- <b><code>&nbsp;&nbsp;3991⭐</code></b> <b><code>&nbsp;&nbsp;1141🍴</code></b> [warehouse](https://github.com/pypa/warehouse)) - Next generation Python Package Repository (PyPI).

## Distribution

_Libraries to create packaged executables for release distribution._

- <b><code>&nbsp;&nbsp;1534⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;239🍴</code></b> [cx-Freeze](https://github.com/marcelotduarte/cx_Freeze)) - It is a Python tool that converts Python scripts into standalone executables and installers for Windows, macOS, and Linux.
- <b><code>&nbsp;14673⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;769🍴</code></b> [Nuitka](https://github.com/Nuitka/Nuitka)) - Compiles Python programs into high-performance standalone executables (cross-platform, supports all Python versions).
- <b><code>&nbsp;&nbsp;4998⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;354🍴</code></b> [pyarmor](https://github.com/dashingsoft/pyarmor)) - A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.
- <b><code>&nbsp;12934⭐</code></b> <b><code>&nbsp;&nbsp;2016🍴</code></b> [pyinstaller](https://github.com/pyinstaller/pyinstaller)) - Converts Python programs into stand-alone executables (cross-platform).
- <b><code>&nbsp;&nbsp;1921⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;109🍴</code></b> [shiv](https://github.com/linkedin/shiv)) - A command line utility for building fully self-contained zipapps (PEP 441), but with all their dependencies included.

## Configuration Files

_Libraries for storing and parsing configuration options._

- 🌎 [configparser](docs.python.org/3/library/configparser.html) - (Python standard library) INI file parser.
- <b><code>&nbsp;&nbsp;4276⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;315🍴</code></b> [dynaconf](https://github.com/dynaconf/dynaconf)) - Dynaconf is a configuration manager with plugins for Django, Flask and FastAPI.
- <b><code>&nbsp;10271⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;822🍴</code></b> [hydra](https://github.com/facebookresearch/hydra)) - Hydra is a framework for elegantly configuring complex applications.
- <b><code>&nbsp;&nbsp;3021⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;212🍴</code></b> [python-decouple](https://github.com/HBNetwork/python-decouple)) - Strict separation of settings from code.
- <b><code>&nbsp;&nbsp;8711⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;514🍴</code></b> [python-dotenv](https://github.com/theskumar/python-dotenv)) - Reads key-value pairs from a `.env` file and sets them as environment variables.

**Security**

## Cryptography

- <b><code>&nbsp;&nbsp;7526⭐</code></b> <b><code>&nbsp;&nbsp;1731🍴</code></b> [cryptography](https://github.com/pyca/cryptography)) - A package designed to expose cryptographic primitives and recipes to Python developers.
- <b><code>&nbsp;&nbsp;9716⭐</code></b> <b><code>&nbsp;&nbsp;2040🍴</code></b> [paramiko](https://github.com/paramiko/paramiko)) - The leading native Python SSHv2 protocol library.
- <b><code>&nbsp;&nbsp;1186⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;254🍴</code></b> [pynacl](https://github.com/pyca/pynacl)) - Python binding to the Networking and Cryptography (NaCl) library.

## Penetration Testing

_Frameworks and tools for penetration testing._

- <b><code>&nbsp;42854⭐</code></b> <b><code>&nbsp;&nbsp;4502🍴</code></b> [mitmproxy](https://github.com/mitmproxy/mitmproxy)) - An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.
- <b><code>&nbsp;14710⭐</code></b> <b><code>&nbsp;&nbsp;3336🍴</code></b> [setoolkit](https://github.com/trustedsec/social-engineer-toolkit)) - A toolkit for social engineering.
- <b><code>&nbsp;74243⭐</code></b> <b><code>&nbsp;&nbsp;8817🍴</code></b> [sherlock](https://github.com/sherlock-project/sherlock)) - Hunt down social media accounts by username across social networks.
- <b><code>&nbsp;36949⭐</code></b> <b><code>&nbsp;&nbsp;6235🍴</code></b> [sqlmap](https://github.com/sqlmapproject/sqlmap)) - Automatic SQL injection and database takeover tool.

**Miscellaneous**

## Hardware

_Libraries for programming with hardware._

- <b><code>&nbsp;&nbsp;2365⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;349🍴</code></b> [bleak](https://github.com/hbldh/bleak)) - A cross platform Bluetooth Low Energy Client for Python using asyncio.
- <b><code>&nbsp;&nbsp;2127⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;283🍴</code></b> [pynput](https://github.com/moses-palmer/pynput)) - A library to control and monitor input devices.

## Microsoft Windows

_Python programming on Microsoft Windows._

- <b><code>&nbsp;&nbsp;5424⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;774🍴</code></b> [pythonnet](https://github.com/pythonnet/pythonnet)) - Python Integration with the .NET Common Language Runtime (CLR).
- <b><code>&nbsp;&nbsp;5535⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;852🍴</code></b> [pywin32](https://github.com/mhammond/pywin32)) - Python Extensions for Windows.
- <b><code>&nbsp;&nbsp;2237⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;347🍴</code></b> [winpython](https://github.com/winpython/winpython)) - Portable development environment for Windows 10/11.

## Miscellaneous

_Useful libraries or tools that don't fit in the categories above._

- <b><code>&nbsp;&nbsp;2037⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;188🍴</code></b> [blinker](https://github.com/jek/blinker)) - A fast Python in-process signal/event dispatching system.
- <b><code>&nbsp;&nbsp;6862⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;387🍴</code></b> [boltons](https://github.com/mahmoud/boltons)) - A set of pure-Python utilities.
- <b><code>&nbsp;&nbsp;3104⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;233🍴</code></b> [itsdangerous](https://github.com/pallets/itsdangerous)) - Various helpers to pass trusted data to untrusted environments.
- <b><code>&nbsp;&nbsp;&nbsp;172⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;68🍴</code></b> [tryton](https://github.com/tryton/tryton)) - A general-purpose business framework.

# Resources

Where to discover learning resources or new Python libraries.

## Newsletters

- [Awesome Python Newsletter](http://python.libhunt.com/newsletter)
- 🌎 [Pycoder's Weekly](pycoders.com/)
- 🌎 [Python Tricks](realpython.com/python-tricks/)
- 🌎 [Python Weekly](www.pythonweekly.com/)

## Podcasts

- 🌎 [Django Chat](djangochat.com/)
- 🌎 [PyPodcats](pypodcats.live)
- 🌎 [Python Bytes](pythonbytes.fm)
- 🌎 [Talk Python To Me](talkpython.fm/)
- 🌎 [The Real Python Podcast](realpython.com/podcasts/rpp/)

# Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](https://github.com/correia-jpv/fucking-awesome-python/blob/master/CONTRIBUTING.md) first.

---

If you have any question about this opinionated list, do not hesitate to contact 🌎 [@vinta](x.com/vinta) on X (Twitter).

## Source
<b><code>289637⭐</code></b> <b><code>&nbsp;27515🍴</code></b> [vinta/awesome-python](https://github.com/vinta/awesome-python))