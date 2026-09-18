# 🌎 [Awesome Python](awesome-python.com/)

An opinionated guide to the best Python frameworks, libraries, and tools.

**Visit the 🌎 [website](awesome-python.com/) to search and filter projects more easily.**

## **Sponsors**

> The **#10 most-starred repo on GitHub**. Put your product in front of Python developers. [Become a sponsor](SPONSORSHIP.md).

## Categories

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
- [ERP](#erp)
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
- [Data Ingestion / ETL](#data-ingestion--etl)
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
- [Messaging](#messaging)
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
- [Supply Chain Security](#supply-chain-security)
- [Web Security](#web-security)

**Other**

- [Hardware](#hardware)
- [Microsoft Windows](#microsoft-windows)
- [Miscellaneous](#miscellaneous)

## Projects

**AI & ML**

### AI and Agents

_Libraries for building AI applications, LLM integrations, and autonomous agents._

- Agent Skills
  - <b><code>&nbsp;&nbsp;&nbsp;141⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;23🍴</code></b> [django-ai-plugins](https://github.com/vintasoftware/django-ai-plugins)) - Django backend agent skills for Django, DRF, Celery, and Django-specific code review.
  - <b><code>&nbsp;&nbsp;&nbsp;995⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;52🍴</code></b> [sentry-skills](https://github.com/getsentry/skills)) - Python-focused engineering skills for code review, debugging, and backend workflows.
  - <b><code>&nbsp;&nbsp;7139⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;611🍴</code></b> [trailofbits-skills](https://github.com/trailofbits/skills)) - Python-friendly security skills for auditing, testing, and safer backend development.
- Orchestration
  - <b><code>146559⭐</code></b> <b><code>&nbsp;24508🍴</code></b> [langchain](https://github.com/langchain-ai/langchain)) - Building applications with LLMs through composability.
  - <b><code>&nbsp;41861⭐</code></b> <b><code>&nbsp;&nbsp;7069🍴</code></b> [langgraph](https://github.com/langchain-ai/langgraph)) - Low-level orchestration framework for building stateful, long-running LLM agents.
  - <b><code>&nbsp;58716⭐</code></b> <b><code>&nbsp;&nbsp;8496🍴</code></b> [crewai](https://github.com/crewAIInc/crewAI)) - A framework for orchestrating role-playing autonomous AI agents for collaborative task solving.
  - <b><code>&nbsp;20019⭐</code></b> <b><code>&nbsp;&nbsp;2730🍴</code></b> [pydantic-ai](https://github.com/pydantic/pydantic-ai)) - A Python agent framework for building generative AI applications with structured schemas.
- Vendor Agent SDKs
  - <b><code>&nbsp;29531⭐</code></b> <b><code>&nbsp;&nbsp;4761🍴</code></b> [openai-agents](https://github.com/openai/openai-agents-python)) - OpenAI's framework for building and managing AI agents.
  - <b><code>&nbsp;&nbsp;8123⭐</code></b> <b><code>&nbsp;&nbsp;1279🍴</code></b> [claude-agent-sdk](https://github.com/anthropics/claude-agent-sdk-python)) - Anthropic's Python SDK for building AI agents on Claude Code's harness — custom tools, in-process MCP servers, hooks.
- Personal Assistants
  - <b><code>246594⭐</code></b> <b><code>&nbsp;51653🍴</code></b> [hermes-agent](https://github.com/nousresearch/hermes-agent)) - An adaptive personal AI assistant that grows with you.
- Prompt Optimization
  - <b><code>&nbsp;38113⭐</code></b> <b><code>&nbsp;&nbsp;3324🍴</code></b> [dspy](https://github.com/stanfordnlp/dspy)) - A framework for programming, not prompting, language models.
- Data Layer
  - <b><code>&nbsp;13915⭐</code></b> <b><code>&nbsp;&nbsp;1253🍴</code></b> [instructor](https://github.com/567-labs/instructor)) - A library for extracting structured data from LLMs, powered by Pydantic.
  - <b><code>&nbsp;52205⭐</code></b> <b><code>&nbsp;&nbsp;8166🍴</code></b> [llama-index](https://github.com/run-llama/llama_index)) - A data framework for your LLM application.
  - <b><code>&nbsp;65533⭐</code></b> <b><code>&nbsp;&nbsp;7686🍴</code></b> [mem0](https://github.com/mem0ai/mem0)) - An intelligent memory layer for AI agents enabling personalized interactions.
  - <b><code>&nbsp;37907⭐</code></b> <b><code>&nbsp;&nbsp;2937🍴</code></b> [openviking](https://github.com/volcengine/OpenViking)) - A context database for AI agents that unifies memory, resources, and skills.
  - <b><code>&nbsp;13112⭐</code></b> <b><code>&nbsp;&nbsp;1462🍴</code></b> [semantica](https://github.com/semantica-agi/semantica)) - A graph-native context and knowledge layer for AI agents with reasoning, provenance, and governance.
- Pre-trained Models
  - <b><code>166261⭐</code></b> <b><code>&nbsp;34619🍴</code></b> [transformers](https://github.com/huggingface/transformers)) - A framework that lets you easily use pre-trained transformer models for NLP, vision, and audio tasks.
- LLM Inference and Serving
  - <b><code>&nbsp;36115⭐</code></b> <b><code>&nbsp;&nbsp;8956🍴</code></b> [sglang](https://github.com/sgl-project/sglang)) - A high-performance serving framework for large language models and multimodal models.
  - <b><code>&nbsp;92047⭐</code></b> <b><code>&nbsp;22346🍴</code></b> [vllm](https://github.com/vllm-project/vllm)) - A high-throughput and memory-efficient inference and serving engine for LLMs.
  - <b><code>&nbsp;&nbsp;7043⭐</code></b> <b><code>&nbsp;&nbsp;1054🍴</code></b> [mlx-lm](https://github.com/ml-explore/mlx-lm)) - Run and fine-tune large language models on Apple Silicon with MLX.
- LLM Gateways
  - <b><code>&nbsp;59030⭐</code></b> <b><code>&nbsp;11542🍴</code></b> [LiteLLM](https://github.com/BerriAI/litellm)) - Call 100+ LLMs using OpenAI format.
- Image and Video Generation
  - <b><code>&nbsp;34534⭐</code></b> <b><code>&nbsp;&nbsp;7329🍴</code></b> [diffusers](https://github.com/huggingface/diffusers)) - A library that provides pre-trained diffusion models for generating and editing images, audio, and video.
- Fine-tuning
  - <b><code>&nbsp;21692⭐</code></b> <b><code>&nbsp;&nbsp;2508🍴</code></b> [peft](https://github.com/huggingface/peft)) - A library for parameter-efficient fine-tuning of large pretrained models.
  - <b><code>&nbsp;76325⭐</code></b> <b><code>&nbsp;&nbsp;6957🍴</code></b> [unsloth](https://github.com/unslothai/unsloth)) - A library for faster LLM fine-tuning and training with reduced memory usage.
  - <b><code>&nbsp;12485⭐</code></b> <b><code>&nbsp;&nbsp;1436🍴</code></b> [axolotl](https://github.com/axolotl-ai-cloud/axolotl)) - A framework for fine-tuning and post-training large language models.
- Speech
  - <b><code>109302⭐</code></b> <b><code>&nbsp;13250🍴</code></b> [openai-whisper](https://github.com/openai/whisper)) - A general-purpose automatic speech recognition model trained on 680k hours of multilingual and multitask supervised data.
  - <b><code>&nbsp;20399⭐</code></b> <b><code>&nbsp;&nbsp;2035🍴</code></b> [funasr](https://github.com/modelscope/FunASR)) - Industrial-grade speech recognition toolkit with 170x realtime speed, 50+ languages, speaker diarization, and emotion detection.
  - <b><code>&nbsp;54383⭐</code></b> <b><code>&nbsp;&nbsp;6122🍴</code></b> [vibevoice](https://github.com/microsoft/VibeVoice)) - A family of open-source voice AI models from Microsoft for text-to-speech and long-form speech recognition.
  - <b><code>&nbsp;&nbsp;2635⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;390🍴</code></b> [gTTS](https://github.com/pndurette/gTTS)) - Python library and CLI tool for converting text to speech using Google Translate TTS.
  - <b><code>&nbsp;15467⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;885🍴</code></b> [kittentts](https://github.com/KittenML/KittenTTS)) - Lightweight ONNX text-to-speech library with small CPU-friendly models.

### Deep Learning

_Frameworks for Neural Networks and Deep Learning. Also see <b><code>&nbsp;28934⭐</code></b> <b><code>&nbsp;&nbsp;6351🍴</code></b> [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning))._

- Frameworks
  - <b><code>103076⭐</code></b> <b><code>&nbsp;29656🍴</code></b> [pytorch](https://github.com/pytorch/pytorch)) - Tensors and Dynamic neural networks in Python with strong GPU acceleration.
  - <b><code>200161⭐</code></b> <b><code>&nbsp;76717🍴</code></b> [tensorflow](https://github.com/tensorflow/tensorflow)) - The most popular Deep Learning framework created by Google.
  - <b><code>&nbsp;64320⭐</code></b> <b><code>&nbsp;19796🍴</code></b> [keras](https://github.com/keras-team/keras)) - A high-level deep learning library with support for JAX, TensorFlow, and PyTorch backends.
  - <b><code>&nbsp;36308⭐</code></b> <b><code>&nbsp;&nbsp;3784🍴</code></b> [jax](https://github.com/jax-ml/jax)) - A library for high-performance numerical computing with automatic differentiation and JIT compilation.
  - <b><code>&nbsp;31349⭐</code></b> <b><code>&nbsp;&nbsp;3795🍴</code></b> [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)) - Deep learning framework to train, deploy, and ship AI products Lightning fast.
- Reinforcement Learning
  - <b><code>&nbsp;12543⭐</code></b> <b><code>&nbsp;&nbsp;1472🍴</code></b> [gymnasium](https://github.com/Farama-Foundation/Gymnasium)) - A standard API for reinforcement learning environments with popular reference environments (<b><code>&nbsp;37240⭐</code></b> <b><code>&nbsp;&nbsp;8675🍴</code></b> [gym](https://github.com/openai/gym)) successor).
  - <b><code>&nbsp;13817⭐</code></b> <b><code>&nbsp;&nbsp;2182🍴</code></b> [stable-baselines3](https://github.com/DLR-RM/stable-baselines3)) - PyTorch implementations of Stable Baselines (deep) reinforcement learning algorithms.

### Machine Learning

_Libraries for Machine Learning. Also see <b><code>&nbsp;74361⭐</code></b> <b><code>&nbsp;15650🍴</code></b> [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python))._

- General
  - <b><code>&nbsp;67286⭐</code></b> <b><code>&nbsp;27421🍴</code></b> [scikit-learn](https://github.com/scikit-learn/scikit-learn)) - The most popular Python library for Machine Learning with extensive documentation and community support.
  - <b><code>&nbsp;&nbsp;3330⭐</code></b> <b><code>&nbsp;&nbsp;1166🍴</code></b> [pgmpy](https://github.com/pgmpy/pgmpy)) - A Python library for probabilistic graphical models and Bayesian networks.
  - <b><code>&nbsp;&nbsp;2280⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;371🍴</code></b> [feature-engine](https://github.com/feature-engine/feature_engine)) - sklearn compatible API with the widest toolset for feature engineering and selection.
- Gradient Boosting
  - <b><code>&nbsp;28776⭐</code></b> <b><code>&nbsp;&nbsp;8900🍴</code></b> [xgboost](https://github.com/dmlc/xgboost)) - A scalable, portable, and distributed gradient boosting library.
  - <b><code>&nbsp;18773⭐</code></b> <b><code>&nbsp;&nbsp;4071🍴</code></b> [lightgbm](https://github.com/lightgbm-org/LightGBM)) - A fast, distributed, high performance gradient boosting framework.
  - <b><code>&nbsp;&nbsp;9105⭐</code></b> <b><code>&nbsp;&nbsp;1334🍴</code></b> [catboost](https://github.com/catboost/catboost)) - A fast, scalable, high performance gradient boosting on decision trees library.
- Time Series Forecasting
  - <b><code>&nbsp;33036⭐</code></b> <b><code>&nbsp;&nbsp;3181🍴</code></b> [timesfm](https://github.com/google-research/timesfm)) - A pretrained foundation model from Google Research for time-series forecasting.

### Natural Language Processing

_Libraries for working with human languages._

- General
  - <b><code>&nbsp;14719⭐</code></b> <b><code>&nbsp;&nbsp;3038🍴</code></b> [nltk](https://github.com/nltk/nltk)) - A leading platform for building Python programs to work with human language data.
  - <b><code>&nbsp;33906⭐</code></b> <b><code>&nbsp;&nbsp;4723🍴</code></b> [spacy](https://github.com/explosion/spaCy)) - A library for industrial-strength natural language processing in Python and Cython.
  - <b><code>&nbsp;16485⭐</code></b> <b><code>&nbsp;&nbsp;4401🍴</code></b> [gensim](https://github.com/piskvorky/gensim)) - Topic Modeling for Humans.
  - <b><code>&nbsp;&nbsp;7878⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;959🍴</code></b> [stanza](https://github.com/stanfordnlp/stanza)) - The Stanford NLP Group's official Python library, supporting 60+ languages.
- Chinese
  - <b><code>&nbsp;35155⭐</code></b> <b><code>&nbsp;&nbsp;6680🍴</code></b> [jieba](https://github.com/fxsjy/jieba)) - The most popular Chinese text segmentation library.
  - <b><code>&nbsp;&nbsp;5362⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;628🍴</code></b> [pypinyin](https://github.com/mozillazg/python-pinyin)) - Convert Chinese hanzi (漢字) to pinyin (拼音).
  - <b><code>&nbsp;&nbsp;&nbsp;278⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [pangu.py](https://github.com/vinta/pangu.py)) - Paranoid text spacing.

### Computer Vision

_Libraries for Computer Vision._

- General
  - <b><code>&nbsp;&nbsp;5394⭐</code></b> <b><code>&nbsp;&nbsp;1041🍴</code></b> [opencv-python](https://github.com/opencv/opencv-python)) - Open Source Computer Vision Library.
  - <b><code>&nbsp;61733⭐</code></b> <b><code>&nbsp;11777🍴</code></b> [ultralytics](https://github.com/ultralytics/ultralytics)) - Ultralytics YOLO for object detection, segmentation, pose estimation, and classification with state-of-the-art accuracy and speed.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [kornia](https://github.com/kornia/kornia/)) - Open Source Differentiable Computer Vision Library for PyTorch.
  - <b><code>&nbsp;11094⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;822🍴</code></b> [fiftyone](https://github.com/voxel51/fiftyone)) - The open-source tool for building high-quality datasets and computer vision models.
- OCR
  - <b><code>&nbsp;&nbsp;6388⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;749🍴</code></b> [pytesseract](https://github.com/madmaze/pytesseract)) - A wrapper for [Google Tesseract OCR](https://github.com/tesseract-ocr).
  - <b><code>&nbsp;29999⭐</code></b> <b><code>&nbsp;&nbsp;3607🍴</code></b> [easyocr](https://github.com/JaidedAI/EasyOCR)) - Ready-to-use OCR with 40+ languages supported.

### Recommender Systems

_Libraries for building recommender systems._

- <b><code>&nbsp;14300⭐</code></b> <b><code>&nbsp;&nbsp;1228🍴</code></b> [annoy](https://github.com/spotify/annoy)) - Approximate Nearest Neighbors in C++/Python optimized for memory usage.
- <b><code>&nbsp;&nbsp;3823⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;631🍴</code></b> [implicit](https://github.com/benfred/implicit)) - A fast Python implementation of collaborative filtering for implicit datasets.
- <b><code>&nbsp;&nbsp;6818⭐</code></b> <b><code>&nbsp;&nbsp;1049🍴</code></b> [scikit-surprise](https://github.com/NicolasHug/Surprise)) - A scikit for building and analyzing recommender systems.

**Web Development**

### Web Frameworks

_Traditional full stack web frameworks. Also see [Web APIs](#web-apis)._

- Synchronous
  - <b><code>&nbsp;74748⭐</code></b> <b><code>&nbsp;16981🍴</code></b> [flask](https://github.com/pallets/flask)) - A microframework for Python.
    - <b><code>&nbsp;12768⭐</code></b> <b><code>&nbsp;&nbsp;1567🍴</code></b> [awesome-flask](https://github.com/humiaozuzu/awesome-flask))
  - <b><code>&nbsp;91128⭐</code></b> <b><code>&nbsp;34657🍴</code></b> [django](https://github.com/django/django)) - The most popular web framework in Python.
    - <b><code>&nbsp;11249⭐</code></b> <b><code>&nbsp;&nbsp;1474🍴</code></b> [awesome-django](https://github.com/wsvincent/awesome-django))
  - <b><code>&nbsp;&nbsp;8789⭐</code></b> <b><code>&nbsp;&nbsp;1509🍴</code></b> [bottle](https://github.com/bottlepy/bottle)) - A fast and simple micro-framework distributed as a single file with no dependencies.
  - <b><code>&nbsp;&nbsp;4100⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;891🍴</code></b> [pyramid](https://github.com/Pylons/pyramid)) - A small, fast, down-to-earth, open source Python web framework.
    - <b><code>&nbsp;&nbsp;&nbsp;573⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;55🍴</code></b> [awesome-pyramid](https://github.com/uralbash/awesome-pyramid))
  - <b><code>&nbsp;&nbsp;7032⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;321🍴</code></b> [fasthtml](https://github.com/AnswerDotAI/fasthtml)) - The fastest way to create an HTML app.
    - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;85⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8🍴</code></b> [awesome-fasthtml](https://github.com/amosgyamfi/awesome-fasthtml))
- Asynchronous
  - <b><code>&nbsp;12618⭐</code></b> <b><code>&nbsp;&nbsp;1312🍴</code></b> [starlette](https://github.com/Kludex/starlette)) - A lightweight ASGI framework and toolkit for building high-performance async services.
  - <b><code>&nbsp;22179⭐</code></b> <b><code>&nbsp;&nbsp;5555🍴</code></b> [tornado](https://github.com/tornadoweb/tornado)) - A web framework and asynchronous networking library.
  - <b><code>&nbsp;&nbsp;8470⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;647🍴</code></b> [litestar](https://github.com/litestar-org/litestar)) - Production-ready, capable and extensible ASGI Web framework.
  - <b><code>&nbsp;28889⭐</code></b> <b><code>&nbsp;&nbsp;1777🍴</code></b> [reflex](https://github.com/reflex-dev/reflex)) - A framework for building reactive, full-stack web applications entirely with Python.

### Web APIs

_Libraries for building RESTful, GraphQL, and RPC APIs._

- Django
  - <b><code>&nbsp;30183⭐</code></b> <b><code>&nbsp;&nbsp;7079🍴</code></b> [django-rest-framework](https://github.com/encode/django-rest-framework)) - A powerful and flexible toolkit to build web APIs.
  - <b><code>&nbsp;&nbsp;9191⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;613🍴</code></b> [django-ninja](https://github.com/vitalik/django-ninja)) - Fast, Django REST framework based on type hints and Pydantic.
  - <b><code>&nbsp;&nbsp;&nbsp;504⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;157🍴</code></b> [strawberry-django](https://github.com/strawberry-graphql/strawberry-django)) - Strawberry GraphQL integration with Django.
  - <b><code>&nbsp;&nbsp;1459⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;208🍴</code></b> [django-modern-rest](https://github.com/wemake-services/django-modern-rest)) - Modern REST with speed, types, async, `msgspec`, `pydantic` and other goodies!
- Flask
  - <b><code>&nbsp;&nbsp;1137⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;143🍴</code></b> [apiflask](https://github.com/apiflask/apiflask)) - A lightweight Python web API framework based on Flask and Marshmallow.
- Framework Agnostic
  - <b><code>102406⭐</code></b> <b><code>&nbsp;&nbsp;9904🍴</code></b> [fastapi](https://github.com/fastapi/fastapi)) - A modern, fast, web framework for building APIs with standard Python type hints.
  - <b><code>&nbsp;&nbsp;4612⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;784🍴</code></b> [connexion](https://github.com/spec-first/connexion)) - A spec-first framework that automatically handles requests based on your OpenAPI specification.
  - <b><code>&nbsp;&nbsp;4719⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;660🍴</code></b> [strawberry](https://github.com/strawberry-graphql/strawberry)) - A GraphQL library that leverages Python type annotations for schema definition.
- RPC
  - <b><code>&nbsp;45321⭐</code></b> <b><code>&nbsp;11368🍴</code></b> [grpcio](https://github.com/grpc/grpc)) - HTTP/2-based RPC framework with Python bindings, built by Google.

### Web Servers

_ASGI and WSGI compatible web servers._

- ASGI
  - <b><code>&nbsp;10970⭐</code></b> <b><code>&nbsp;&nbsp;1029🍴</code></b> [uvicorn](https://github.com/Kludex/uvicorn)) - A lightning-fast ASGI server implementation, using uvloop and httptools.
  - <b><code>&nbsp;&nbsp;5653⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;174🍴</code></b> [granian](https://github.com/emmett-framework/granian)) - A Rust HTTP server for Python applications built on top of Hyper and Tokio, supporting WSGI/ASGI/RSGI.
  - <b><code>&nbsp;&nbsp;1611⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;165🍴</code></b> [hypercorn](https://github.com/pgjones/hypercorn)) - An ASGI and WSGI Server based on Hyper libraries and inspired by Gunicorn.
- WSGI
  - <b><code>&nbsp;10675⭐</code></b> <b><code>&nbsp;&nbsp;1864🍴</code></b> [gunicorn](https://github.com/benoitc/gunicorn)) - Pre-forked, ported from Ruby's Unicorn project.
  - <b><code>&nbsp;&nbsp;1600⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;190🍴</code></b> [waitress](https://github.com/Pylons/waitress)) - Multi-threaded, powers Pyramid.

### WebSocket

_Libraries for working with WebSocket._

- <b><code>&nbsp;&nbsp;5717⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;612🍴</code></b> [websockets](https://github.com/python-websockets/websockets)) - A library for building WebSocket servers and clients with a focus on correctness and simplicity.
- <b><code>&nbsp;&nbsp;6358⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;826🍴</code></b> [channels](https://github.com/django/channels)) - Developer-friendly asynchrony for Django.
- <b><code>&nbsp;&nbsp;5507⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;903🍴</code></b> [flask-socketio](https://github.com/miguelgrinberg/Flask-SocketIO)) - Socket.IO integration for Flask applications.
- <b><code>&nbsp;&nbsp;2543⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;768🍴</code></b> [autobahn-python](https://github.com/crossbario/autobahn-python)) - WebSocket & WAMP for Python on Twisted and 🌎 [asyncio](docs.python.org/3/library/asyncio.html).

### Template Engines

_Libraries and tools for templating and lexing._

- <b><code>&nbsp;11779⭐</code></b> <b><code>&nbsp;&nbsp;1828🍴</code></b> [jinja](https://github.com/pallets/jinja)) - A modern and designer friendly templating language.
- <b><code>&nbsp;&nbsp;&nbsp;459⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;89🍴</code></b> [mako](https://github.com/sqlalchemy/mako)) - Hyperfast and lightweight templating for the Python platform.

### Web Asset Management

_Tools for managing, storing, compressing and minifying website assets._

- <b><code>&nbsp;&nbsp;2958⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;895🍴</code></b> [django-storages](https://github.com/jschneier/django-storages)) - A collection of custom storage back ends for Django.
- <b><code>&nbsp;&nbsp;2869⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;604🍴</code></b> [django-compressor](https://github.com/django-compressor/django-compressor)) - Compresses linked and inline JavaScript or CSS into a single cached file.

### Authentication

_Libraries for implementing authentication schemes._

- OAuth
  - <b><code>&nbsp;&nbsp;2980⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;529🍴</code></b> [oauthlib](https://github.com/oauthlib/oauthlib)) - A generic and thorough implementation of the OAuth request-signing logic.
  - <b><code>&nbsp;&nbsp;5424⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;563🍴</code></b> [authlib](https://github.com/authlib/authlib)) - A comprehensive library for building OAuth, OpenID Connect, and JWT/JWS/JWE/JWK/JWA.
  - <b><code>&nbsp;10378⭐</code></b> <b><code>&nbsp;&nbsp;3107🍴</code></b> [django-allauth](https://github.com/pennersr/django-allauth)) - Authentication app for Django that "just works."
  - <b><code>&nbsp;&nbsp;3335⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;857🍴</code></b> [django-oauth-toolkit](https://github.com/django-oauth/django-oauth-toolkit)) - OAuth 2 goodies for Django.
- JWT
  - <b><code>&nbsp;&nbsp;5700⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;796🍴</code></b> [pyjwt](https://github.com/jpadilla/pyjwt)) - JSON Web Token implementation in Python.
- Permissions
  - <b><code>&nbsp;&nbsp;3913⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;595🍴</code></b> [django-guardian](https://github.com/django-guardian/django-guardian)) - Implementation of per-object permissions for Django.
  - <b><code>&nbsp;&nbsp;1975⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [django-rules](https://github.com/dfunckt/django-rules)) - A tiny but powerful app providing object-level permissions to Django, without requiring a database.

### Admin Panels

_Libraries for administrative interfaces._

- <b><code>&nbsp;&nbsp;6068⭐</code></b> <b><code>&nbsp;&nbsp;1644🍴</code></b> [flask-admin](https://github.com/pallets-eco/flask-admin)) - Simple and extensible administrative interface framework for Flask.
- <b><code>&nbsp;&nbsp;3680⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;369🍴</code></b> [django-unfold](https://github.com/unfoldadmin/django-unfold)) - Elevate your Django admin with a stunning modern interface, powerful features, and seamless user experience.
- <b><code>&nbsp;&nbsp;3947⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;649🍴</code></b> [django-grappelli](https://github.com/sehmaschine/django-grappelli)) - A jazzy skin for the Django Admin-Interface.

### CMS

_Content Management Systems._

- <b><code>&nbsp;20503⭐</code></b> <b><code>&nbsp;&nbsp;4609🍴</code></b> [wagtail](https://github.com/wagtail/wagtail)) - A Django content management system.
- <b><code>&nbsp;10669⭐</code></b> <b><code>&nbsp;&nbsp;3194🍴</code></b> [django-cms](https://github.com/django-cms/django-cms)) - The easy-to-use and developer-friendly enterprise CMS powered by Django.

### ERP

_Enterprise resource planning frameworks._

- <b><code>&nbsp;54433⭐</code></b> <b><code>&nbsp;33745🍴</code></b> [odoo](https://github.com/odoo/odoo)) - A suite of open source business apps: CRM, e-commerce, accounting, inventory, and thousands of community modules.

### Static Site Generators

_Static site generator is a software that takes some text + templates as input and produces HTML files on the output._

- <b><code>&nbsp;13341⭐</code></b> <b><code>&nbsp;&nbsp;1822🍴</code></b> [pelican](https://github.com/getpelican/pelican)) - Static site generator that supports Markdown and reST syntax.
- <b><code>&nbsp;&nbsp;2742⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;471🍴</code></b> [nikola](https://github.com/getnikola/nikola)) - A static website and blog generator.

**HTTP & Scraping**

### HTTP Clients

_Libraries for working with HTTP._

- Clients
  - <b><code>&nbsp;54318⭐</code></b> <b><code>&nbsp;10288🍴</code></b> [requests](https://github.com/psf/requests)) - HTTP Requests for Humans.
  - <b><code>&nbsp;15495⭐</code></b> <b><code>&nbsp;&nbsp;1445🍴</code></b> [httpx](https://github.com/encode/httpx)) - A next generation HTTP client for Python.
  - <b><code>&nbsp;16549⭐</code></b> <b><code>&nbsp;&nbsp;2412🍴</code></b> [aiohttp](https://github.com/aio-libs/aiohttp)) - Asynchronous HTTP client/server framework for asyncio and Python.
  - <b><code>&nbsp;&nbsp;4058⭐</code></b> <b><code>&nbsp;&nbsp;1581🍴</code></b> [urllib3](https://github.com/urllib3/urllib3)) - A HTTP library with thread-safe connection pooling, file post support, sanity friendly.
  - <b><code>&nbsp;&nbsp;1452⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;74🍴</code></b> [httpx2](https://github.com/pydantic/httpx2)) - HTTP/1.1 and HTTP/2 client with sync and async APIs, maintained by Pydantic (<b><code>&nbsp;15495⭐</code></b> <b><code>&nbsp;&nbsp;1445🍴</code></b> [httpx](https://github.com/encode/httpx)) fork).
- URL Manipulation
  - <b><code>&nbsp;&nbsp;1496⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;216🍴</code></b> [yarl](https://github.com/aio-libs/yarl)) - Yet another URL library.

### Web Scraping

_Libraries to automate web scraping and extract web content._

- Frameworks
  - <b><code>115009⭐</code></b> <b><code>&nbsp;12659🍴</code></b> [browser-use](https://github.com/browser-use/browser-use)) - Make websites accessible for AI agents with easy browser automation.
  - <b><code>&nbsp;64394⭐</code></b> <b><code>&nbsp;11964🍴</code></b> [scrapy](https://github.com/scrapy/scrapy)) - A fast high-level screen scraping and web crawling framework.
  - <b><code>&nbsp;83776⭐</code></b> <b><code>&nbsp;&nbsp;8664🍴</code></b> [crawl4ai](https://github.com/unclecode/crawl4ai)) - An open-source, LLM-friendly web crawler that provides lightning-fast, structured data extraction specifically designed for AI agents.
- Content Extraction
  - <b><code>&nbsp;&nbsp;2423⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;376🍴</code></b> [feedparser](https://github.com/kurtmckee/feedparser)) - Universal feed parser.
  - <b><code>&nbsp;&nbsp;2170⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;297🍴</code></b> [html2text](https://github.com/Alir3z4/html2text)) - Convert HTML to Markdown-formatted text.
  - <b><code>&nbsp;&nbsp;6832⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;431🍴</code></b> [trafilatura](https://github.com/adbar/trafilatura)) - A tool for gathering text and metadata from the web, with built-in content filtering.

### Email

_Libraries for sending and parsing email, and mail server management._

- <b><code>&nbsp;&nbsp;2734⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;265🍴</code></b> [yagmail](https://github.com/kootenpv/yagmail)) - Yet another Gmail/SMTP client.

**Database & Storage**

### ORM

_Libraries that implement Object-Relational Mapping or data mapping techniques._

- Relational Databases
  - <b><code>&nbsp;12165⭐</code></b> <b><code>&nbsp;&nbsp;1784🍴</code></b> [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)) - The Python SQL Toolkit and Object Relational Mapper.
    - <b><code>&nbsp;&nbsp;3058⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;165🍴</code></b> [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy))
  - <b><code>&nbsp;91128⭐</code></b> <b><code>&nbsp;34657🍴</code></b> [django.db.models](https://github.com/django/django)) - (part of Django) The Django 🌎 [ORM](docs.djangoproject.com/en/dev/topics/db/models/).
  - <b><code>&nbsp;11987⭐</code></b> <b><code>&nbsp;&nbsp;1380🍴</code></b> [peewee](https://github.com/coleifer/peewee)) - A small, expressive ORM.
  - <b><code>&nbsp;18330⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;887🍴</code></b> [sqlmodel](https://github.com/fastapi/sqlmodel)) - SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.
- NoSQL Databases
  - <b><code>&nbsp;&nbsp;2647⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;430🍴</code></b> [pynamodb](https://github.com/pynamodb/PynamoDB)) - A Pythonic interface for 🌎 [Amazon DynamoDB](aws.amazon.com/dynamodb/).
  - <b><code>&nbsp;&nbsp;4349⭐</code></b> <b><code>&nbsp;&nbsp;1229🍴</code></b> [mongoengine](https://github.com/MongoEngine/mongoengine)) - A Python Object-Document-Mapper for working with MongoDB.
  - <b><code>&nbsp;&nbsp;2700⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;309🍴</code></b> [beanie](https://github.com/BeanieODM/beanie)) - An asynchronous Python object-document mapper (ODM) for MongoDB.

### Database Drivers

_Libraries for connecting and operating databases._

- MySQL - <b><code>&nbsp;&nbsp;2614⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;412🍴</code></b> [awesome-mysql](https://github.com/shlomi-noach/awesome-mysql))
  - <b><code>&nbsp;&nbsp;7845⭐</code></b> <b><code>&nbsp;&nbsp;1442🍴</code></b> [pymysql](https://github.com/PyMySQL/PyMySQL)) - A pure Python MySQL driver compatible to mysql-python.
  - <b><code>&nbsp;&nbsp;2539⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;443🍴</code></b> [mysqlclient](https://github.com/PyMySQL/mysqlclient)) - MySQL connector with Python 3 support  🌎 [mysql-python](sourceforge.net/projects/mysql-python/) fork).
- PostgreSQL - <b><code>&nbsp;12096⭐</code></b> <b><code>&nbsp;&nbsp;1025🍴</code></b> [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres))
  - <b><code>&nbsp;&nbsp;2500⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;274🍴</code></b> [psycopg](https://github.com/psycopg/psycopg)) - The most popular PostgreSQL adapter for Python.
  - <b><code>&nbsp;&nbsp;8092⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;467🍴</code></b> [asyncpg](https://github.com/MagicStack/asyncpg)) - A fast PostgreSQL Database Client Library for Python/asyncio.
- SQLite - <b><code>&nbsp;&nbsp;&nbsp;405⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;61🍴</code></b> [awesome-sqlite](https://github.com/planetopendata/awesome-sqlite))
  - 🌎 [sqlite3](docs.python.org/3/library/sqlite3.html) - (Python standard library) SQLite interface compliant with DB-API 2.0.
  - <b><code>&nbsp;&nbsp;2170⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;171🍴</code></b> [sqlite-utils](https://github.com/simonw/sqlite-utils)) - Python CLI utility and library for manipulating SQLite databases.
- ClickHouse
  - <b><code>&nbsp;&nbsp;&nbsp;521⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;159🍴</code></b> [clickhouse-connect](https://github.com/ClickHouse/clickhouse-connect)) - The official ClickHouse client, with SQLAlchemy and Superset connectors.
  - <b><code>&nbsp;&nbsp;1303⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;240🍴</code></b> [clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver)) - Python driver with native interface for ClickHouse.
- Other Relational Databases
  - <b><code>&nbsp;&nbsp;3081⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;569🍴</code></b> [pyodbc](https://github.com/mkleehammer/pyodbc)) - An ODBC bridge for connecting to SQL Server and any other ODBC-accessible database.
  - <b><code>&nbsp;&nbsp;&nbsp;451⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [oracledb](https://github.com/oracle/python-oracledb)) - The official Python driver for Oracle Database, successor to cx_Oracle.
  - <b><code>&nbsp;&nbsp;&nbsp;472⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;60🍴</code></b> [mssql-python](https://github.com/microsoft/mssql-python)) - Official Microsoft driver for SQL Server and Azure SQL, built on ODBC for high performance and low memory usage.
- NoSQL Databases
  - <b><code>&nbsp;13644⭐</code></b> <b><code>&nbsp;&nbsp;2747🍴</code></b> [redis](https://github.com/redis/redis-py)) - The Python client for Redis.
  - <b><code>&nbsp;&nbsp;4355⭐</code></b> <b><code>&nbsp;&nbsp;1159🍴</code></b> [pymongo](https://github.com/mongodb/mongo-python-driver)) - The official Python client for MongoDB.
  - <b><code>&nbsp;&nbsp;1427⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;585🍴</code></b> [cassandra-driver](https://github.com/apache/cassandra-python-driver)) - The Python Driver for Apache Cassandra.
  - <b><code>&nbsp;&nbsp;&nbsp;228⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [django-mongodb-backend](https://github.com/mongodb/django-mongodb-backend)) - Official MongoDB database backend for Django.

### Database

_In-process databases usable directly from Python._

- Analytical
  - <b><code>&nbsp;41463⭐</code></b> <b><code>&nbsp;&nbsp;3800🍴</code></b> [duckdb](https://github.com/duckdb/duckdb)) - An in-process SQL OLAP database management system; optimized for analytics and fast queries, similar to SQLite but for analytical workloads.
  - <b><code>&nbsp;&nbsp;2900⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;133🍴</code></b> [chdb](https://github.com/chdb-io/chdb)) - In-process OLAP SQL engine with the full ClickHouse dialect, zero-copy pandas/Arrow interop, and federation to remote ClickHouse clusters via `remoteSecure()`.
- Vector
  - <b><code>&nbsp;29319⭐</code></b> <b><code>&nbsp;&nbsp;2517🍴</code></b> [chromadb](https://github.com/chroma-core/chroma)) - An open-source embedding database for building AI applications with embeddings and semantic search.
  - <b><code>&nbsp;11449⭐</code></b> <b><code>&nbsp;&nbsp;1056🍴</code></b> [lancedb](https://github.com/lancedb/lancedb)) - A developer-friendly embedded retrieval database for multimodal AI.
  - <b><code>&nbsp;15963⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;996🍴</code></b> [zvec](https://github.com/alibaba/zvec)) - An embedded vector database for on-device RAG and edge AI, the SQLite of vector databases.
- Key-Value & Document
  - <b><code>&nbsp;&nbsp;7567⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;629🍴</code></b> [tinydb](https://github.com/msiemens/tinydb)) - A tiny, document-oriented database.

### Caching

_Libraries for caching data._

- <b><code>&nbsp;&nbsp;2777⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;209🍴</code></b> [cachetools](https://github.com/tkem/cachetools)) - Extensible memoizing collections and decorators.
- <b><code>&nbsp;&nbsp;2905⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;186🍴</code></b> [diskcache](https://github.com/grantjenks/python-diskcache)) - SQLite and file backed cache backend with faster lookups than memcached and redis.
- <b><code>&nbsp;&nbsp;&nbsp;411⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;52🍴</code></b> [hishel](https://github.com/karpetrosyan/hishel)) - RFC 9111 compliant HTTP caching for httpx and requests, with sync and async support.
- <b><code>&nbsp;&nbsp;&nbsp;298⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [dogpile.cache](https://github.com/sqlalchemy/dogpile.cache)) - dogpile.cache is a next generation replacement for Beaker made by the same authors.
- <b><code>&nbsp;&nbsp;2273⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;242🍴</code></b> [django-cacheops](https://github.com/Suor/django-cacheops)) - A slick ORM cache with automatic granular event-driven invalidation.

### Search

_Libraries and software for indexing and performing search queries on data._

- <b><code>&nbsp;&nbsp;4386⭐</code></b> <b><code>&nbsp;&nbsp;1220🍴</code></b> [elasticsearch](https://github.com/elastic/elasticsearch-py)) - The official low-level Python client for 🌎 [Elasticsearch](www.elastic.co/products/elasticsearch).
- <b><code>&nbsp;&nbsp;&nbsp;470⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;248🍴</code></b> [opensearch-py](https://github.com/opensearch-project/opensearch-py)) - The official low-level Python client for 🌎 [OpenSearch](opensearch.org/).
- <b><code>&nbsp;&nbsp;&nbsp;602⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;118🍴</code></b> [meilisearch](https://github.com/meilisearch/meilisearch-python)) - The official Python client for the 🌎 [Meilisearch](www.meilisearch.com/) search engine.
- <b><code>&nbsp;&nbsp;3731⭐</code></b> <b><code>&nbsp;&nbsp;1314🍴</code></b> [django-haystack](https://github.com/django-haystack/django-haystack)) - Modular search for Django.

### Serialization

_Libraries for serializing complex data types._

- <b><code>&nbsp;&nbsp;2103⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;259🍴</code></b> [msgpack](https://github.com/msgpack/msgpack-python)) - MessagePack serializer implementation for Python.
- <b><code>&nbsp;&nbsp;8229⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;337🍴</code></b> [orjson](https://github.com/ijl/orjson)) - Fast, correct JSON library.
- <b><code>&nbsp;&nbsp;7238⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;737🍴</code></b> [marshmallow](https://github.com/marshmallow-code/marshmallow)) - A lightweight library for converting complex objects to and from simple Python datatypes.
- <b><code>&nbsp;&nbsp;4113⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;192🍴</code></b> [msgspec](https://github.com/msgspec/msgspec)) - A fast serialization and validation library with built-in support for JSON, MessagePack, YAML, and TOML.

**Data & Science**

### Data Analysis

_Libraries for data analysis._

- <b><code>&nbsp;49740⭐</code></b> <b><code>&nbsp;20395🍴</code></b> [pandas](https://github.com/pandas-dev/pandas)) - A library providing high-performance, easy-to-use data structures and data analysis tools.
- <b><code>&nbsp;39763⭐</code></b> <b><code>&nbsp;&nbsp;3111🍴</code></b> [polars](https://github.com/pola-rs/polars)) - A fast DataFrame library implemented in Rust with a Python API.
- <b><code>&nbsp;&nbsp;6661⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;767🍴</code></b> [ibis-framework](https://github.com/ibis-project/ibis)) - A portable Python dataframe library with a single API for 20+ backends.

### Data Ingestion / ETL

_Libraries for data extraction, transformation, and loading pipelines across multiple sources and destinations._

- General
  - <b><code>&nbsp;&nbsp;4119⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;748🍴</code></b> [awswrangler](https://github.com/aws/aws-sdk-pandas)) - Pandas integration with AWS services like Athena, Glue, Redshift, S3, and DynamoDB.
  - <b><code>&nbsp;&nbsp;5871⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;604🍴</code></b> [dlt](https://github.com/dlt-hub/dlt)) - A Python library for building data pipelines with automatic schema inference, incremental loading, and support for multiple sources and destinations.
  - <b><code>&nbsp;62273⭐</code></b> <b><code>&nbsp;&nbsp;1687🍴</code></b> [pathway](https://github.com/pathwaycom/pathway)) - Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.
- Financial Data
  - <b><code>&nbsp;25280⭐</code></b> <b><code>&nbsp;&nbsp;3421🍴</code></b> [yfinance](https://github.com/ranaroussi/yfinance)) - Easy Pythonic way to download market and financial data from Yahoo Finance.
  - <b><code>&nbsp;22629⭐</code></b> <b><code>&nbsp;&nbsp;3513🍴</code></b> [akshare](https://github.com/akfamily/akshare)) - A financial data interface library, built for human beings!
  - <b><code>&nbsp;&nbsp;2726⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;484🍴</code></b> [edgartools](https://github.com/dgunning/edgartools)) - Library for downloading structured data from SEC EDGAR filings and XBRL financial statements.
  - <b><code>&nbsp;73164⭐</code></b> <b><code>&nbsp;&nbsp;7569🍴</code></b> [openbb](https://github.com/OpenBB-finance/OpenBB)) - A financial data platform for analysts, quants and AI agents.

### Data Validation

_Libraries for validating data. Used for forms in many cases._

- <b><code>&nbsp;28814⭐</code></b> <b><code>&nbsp;&nbsp;2955🍴</code></b> [pydantic](https://github.com/pydantic/pydantic)) - Data validation using Python type hints.
- <b><code>&nbsp;&nbsp;4982⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;668🍴</code></b> [jsonschema](https://github.com/python-jsonschema/jsonschema)) - An implementation of 🌎 [JSON Schema](json-schema.org/) for Python.
- <b><code>&nbsp;&nbsp;4457⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;450🍴</code></b> [pandera](https://github.com/unionai-oss/pandera)) - A data validation library for dataframes, with support for pandas, polars, and Spark.

### Data Visualization

_Libraries for visualizing data. Also see <b><code>&nbsp;35030⭐</code></b> <b><code>&nbsp;&nbsp;4553🍴</code></b> [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization))._

- Plotting
  - <b><code>&nbsp;23229⭐</code></b> <b><code>&nbsp;&nbsp;8485🍴</code></b> [matplotlib](https://github.com/matplotlib/matplotlib)) - A Python 2D plotting library.
  - <b><code>&nbsp;18788⭐</code></b> <b><code>&nbsp;&nbsp;2847🍴</code></b> [plotly](https://github.com/plotly/plotly.py)) - Interactive graphing library for Python.
  - <b><code>&nbsp;14023⭐</code></b> <b><code>&nbsp;&nbsp;2133🍴</code></b> [seaborn](https://github.com/mwaskom/seaborn)) - Statistical data visualization using Matplotlib.
  - <b><code>&nbsp;10477⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;869🍴</code></b> [altair](https://github.com/vega/altair)) - Declarative statistical visualization library for Python.
  - <b><code>&nbsp;20453⭐</code></b> <b><code>&nbsp;&nbsp;4263🍴</code></b> [bokeh](https://github.com/bokeh/bokeh)) - Interactive Web Plotting for Python.
- Specialized
  - <b><code>&nbsp;&nbsp;1618⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;399🍴</code></b> [cartopy](https://github.com/SciTools/cartopy)) - A cartographic python library with matplotlib support.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [pygraphviz](https://github.com/pygraphviz/pygraphviz/)) - Python interface to 🌎 [Graphviz](www.graphviz.org/).
  - <b><code>119108⭐</code></b> <b><code>&nbsp;11516🍴</code></b> [graphify](https://github.com/Graphify-Labs/graphify)) - Turn any folder of code, SQL schemas, docs, papers, images, or videos into a queryable knowledge graph.
- Dashboards and Apps
  - <b><code>&nbsp;45778⭐</code></b> <b><code>&nbsp;&nbsp;4381🍴</code></b> [streamlit](https://github.com/streamlit/streamlit)) - A framework which lets you build dashboards, generate reports, or create chat apps in minutes.
  - <b><code>&nbsp;43563⭐</code></b> <b><code>&nbsp;&nbsp;3601🍴</code></b> [gradio](https://github.com/gradio-app/gradio)) - Build and share machine learning apps, all in Python.

### Geolocation

_Libraries for geocoding addresses and working with latitudes and longitudes._

- <b><code>&nbsp;&nbsp;5250⭐</code></b> <b><code>&nbsp;&nbsp;1059🍴</code></b> [geopandas](https://github.com/geopandas/geopandas)) - Python tools for geographic data (GeoSeries/GeoDataFrame) built on pandas.
- <b><code>&nbsp;&nbsp;4862⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;664🍴</code></b> [geopy](https://github.com/geopy/geopy)) - Python Geocoding Toolbox.
- <b><code>&nbsp;&nbsp;&nbsp;993⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;134🍴</code></b> [geojson](https://github.com/jazzband/geojson)) - Python bindings and utilities for GeoJSON.
- <b><code>&nbsp;91128⭐</code></b> <b><code>&nbsp;34657🍴</code></b> [geodjango](https://github.com/django/django)) - (part of Django) A world-class 🌎 [geographic web framework](docs.djangoproject.com/en/dev/ref/contrib/gis/).

### Science

_Libraries for scientific computing. Also see <b><code>&nbsp;&nbsp;&nbsp;375⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [Python-for-Scientists](https://github.com/TomNicholas/Python-for-Scientists))._

- Core
  - <b><code>&nbsp;32763⭐</code></b> <b><code>&nbsp;12811🍴</code></b> [numpy](https://github.com/numpy/numpy)) - A fundamental package for scientific computing with Python.
  - <b><code>&nbsp;15021⭐</code></b> <b><code>&nbsp;&nbsp;5943🍴</code></b> [scipy](https://github.com/scipy/scipy)) - A Python-based ecosystem of open-source software for mathematics, science, and engineering.
  - <b><code>&nbsp;11156⭐</code></b> <b><code>&nbsp;&nbsp;1323🍴</code></b> [numba](https://github.com/numba/numba)) - Python JIT compiler to LLVM aimed at scientific Python.
- Symbolic Mathematics
  - <b><code>&nbsp;14945⭐</code></b> <b><code>&nbsp;&nbsp;5507🍴</code></b> [sympy](https://github.com/sympy/sympy)) - A Python library for symbolic mathematics.
- Statistics
  - <b><code>&nbsp;11629⭐</code></b> <b><code>&nbsp;&nbsp;3595🍴</code></b> [statsmodels](https://github.com/statsmodels/statsmodels)) - Statistical modeling and econometrics in Python.
- Biology and Chemistry
  - <b><code>&nbsp;&nbsp;5198⭐</code></b> <b><code>&nbsp;&nbsp;1951🍴</code></b> [biopython](https://github.com/biopython/biopython)) - Biopython is a set of freely available tools for biological computation.
  - <b><code>&nbsp;&nbsp;3590⭐</code></b> <b><code>&nbsp;&nbsp;1066🍴</code></b> [rdkit](https://github.com/rdkit/rdkit)) - Cheminformatics and Machine Learning Software.
- Physics and Engineering
  - <b><code>&nbsp;&nbsp;2796⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;536🍴</code></b> [pint](https://github.com/hgrecco/pint)) - Operate and manipulate physical quantities with units and dimensional analysis.
  - <b><code>&nbsp;&nbsp;5308⭐</code></b> <b><code>&nbsp;&nbsp;2169🍴</code></b> [astropy](https://github.com/astropy/astropy)) - A community Python library for Astronomy.
  - <b><code>&nbsp;&nbsp;1333⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;566🍴</code></b> [obspy](https://github.com/obspy/obspy)) - A Python toolbox for seismology.
- Simulation and Modeling
  - <b><code>&nbsp;&nbsp;9755⭐</code></b> <b><code>&nbsp;&nbsp;2301🍴</code></b> [pymc](https://github.com/pymc-devs/pymc)) - Probabilistic programming and Bayesian modeling in Python.
  - 🌎 [simpy](gitlab.com/team-simpy/simpy) - A process-based discrete-event simulation framework.
  - <b><code>&nbsp;&nbsp;3846⭐</code></b> <b><code>&nbsp;&nbsp;1313🍴</code></b> [mesa](https://github.com/mesa/mesa)) - An agent-based modeling framework for building, analyzing, and visualizing complex system simulations.
- Graphs and Networks
  - <b><code>&nbsp;17267⭐</code></b> <b><code>&nbsp;&nbsp;3602🍴</code></b> [networkx](https://github.com/networkx/networkx)) - A high-productivity software for complex networks.
- Computational Geometry
  - <b><code>&nbsp;&nbsp;4511⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;631🍴</code></b> [shapely](https://github.com/shapely/shapely)) - Manipulation and analysis of geometric objects in the Cartesian plane.
- Other
  - <b><code>&nbsp;&nbsp;2651⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;291🍴</code></b> [colour-science](https://github.com/colour-science/colour)) - Implementing a comprehensive number of colour theory transformations and algorithms.
  - <b><code>&nbsp;40902⭐</code></b> <b><code>&nbsp;&nbsp;3116🍴</code></b> [manim](https://github.com/ManimCommunity/manim)) - An animation engine for explanatory math videos.

### Quantum Computing

_Libraries for quantum computing._

- <b><code>&nbsp;&nbsp;7807⭐</code></b> <b><code>&nbsp;&nbsp;3038🍴</code></b> [qiskit](https://github.com/Qiskit/qiskit)) - An IBM-backed quantum SDK for building, simulating, and running circuits on real quantum hardware.
- <b><code>&nbsp;&nbsp;2074⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;783🍴</code></b> [qutip](https://github.com/qutip/qutip)) - Quantum Toolbox in Python.
- <b><code>&nbsp;&nbsp;3472⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;860🍴</code></b> [pennylane](https://github.com/PennyLaneAI/pennylane)) - A hybrid quantum-classical machine learning library with automatic differentiation support.
- <b><code>&nbsp;&nbsp;5062⭐</code></b> <b><code>&nbsp;&nbsp;1267🍴</code></b> [cirq](https://github.com/quantumlib/Cirq)) - A Google-developed framework focused on hardware-aware quantum circuit design for NISQ devices.

**Developer Tools**

### Algorithms and Design Patterns

_Python implementation of data structures, algorithms and design patterns. Also see <b><code>&nbsp;25546⭐</code></b> <b><code>&nbsp;&nbsp;2965🍴</code></b> [awesome-algorithms](https://github.com/tayllan/awesome-algorithms))._

- Algorithms
  - <b><code>&nbsp;&nbsp;3982⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;234🍴</code></b> [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)) - Fast and pure-Python implementation of sorted collections.
  - <b><code>&nbsp;25548⭐</code></b> <b><code>&nbsp;&nbsp;4712🍴</code></b> [algorithms](https://github.com/keon/algorithms)) - Minimal examples of data structures and algorithms.
  - <b><code>224684⭐</code></b> <b><code>&nbsp;51090🍴</code></b> [thealgorithms](https://github.com/TheAlgorithms/Python)) - All Algorithms implemented in Python.
- Design Patterns
  - <b><code>&nbsp;&nbsp;6591⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;569🍴</code></b> [transitions](https://github.com/pytransitions/transitions)) - A lightweight, object-oriented finite state machine implementation.
  - <b><code>&nbsp;42993⭐</code></b> <b><code>&nbsp;&nbsp;6989🍴</code></b> [python-patterns](https://github.com/faif/python-patterns)) - A collection of design patterns in Python.
  - <b><code>&nbsp;&nbsp;1310⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;113🍴</code></b> [python-statemachine](https://github.com/fgmacedo/python-statemachine)) - Expressive statecharts and finite state machines with a declarative API, in sync and async codebases.

### Interactive Interpreter

_Interactive Python interpreters (REPL)._

- <b><code>&nbsp;16784⭐</code></b> <b><code>&nbsp;&nbsp;4518🍴</code></b> [ipython](https://github.com/ipython/ipython)) - A powerful interactive Python shell, and the kernel behind Jupyter notebooks.
- <b><code>&nbsp;13344⭐</code></b> <b><code>&nbsp;&nbsp;5765🍴</code></b> [jupyter](https://github.com/jupyter/notebook)) - A rich toolkit to help you make the most out of using Python interactively.
  - <b><code>&nbsp;&nbsp;4671⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;463🍴</code></b> [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter))
- <b><code>&nbsp;22820⭐</code></b> <b><code>&nbsp;&nbsp;1275🍴</code></b> [marimo](https://github.com/marimo-team/marimo)) - Transform data and train models, feels like a next-gen notebook, stored as Git-friendly Python.
- <b><code>&nbsp;&nbsp;5451⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;293🍴</code></b> [ptpython](https://github.com/prompt-toolkit/ptpython)) - Advanced Python REPL built on top of the <b><code>&nbsp;10575⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;813🍴</code></b> [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)).

### Code Analysis

_Tools of static analysis, linters and code quality checkers. Also see <b><code>&nbsp;14782⭐</code></b> <b><code>&nbsp;&nbsp;1510🍴</code></b> [awesome-static-analysis](https://github.com/analysis-tools-dev/static-analysis))._

- Code Analysis
  - <b><code>&nbsp;&nbsp;1186⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;88🍴</code></b> [import-linter](https://github.com/seddonym/import-linter)) - A linter that enforces architectural constraints on imports between Python modules.
  - <b><code>&nbsp;&nbsp;4812⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;202🍴</code></b> [vulture](https://github.com/jendrikseipp/vulture)) - A tool for finding and analyzing dead Python code.
  - <b><code>&nbsp;&nbsp;&nbsp;855⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [complexipy](https://github.com/rohaquinlop/complexipy)) - Cognitive complexity analysis for Python code, written in Rust.
  - <b><code>&nbsp;&nbsp;2083⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;180🍴</code></b> [prospector](https://github.com/prospector-dev/prospector)) - A tool to analyze Python code.
  - <b><code>&nbsp;&nbsp;6693⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;702🍴</code></b> [repowise](https://github.com/repowise-dev/repowise)) - Codebase intelligence that indexes repos into dependency graphs, git history, and auto-generated docs with dead code detection.
- Git Hooks
  - <b><code>&nbsp;15581⭐</code></b> <b><code>&nbsp;&nbsp;1009🍴</code></b> [pre-commit](https://github.com/pre-commit/pre-commit)) - A framework for managing and maintaining multi-language pre-commit hooks.
- Linters and Formatters
  - <b><code>&nbsp;49674⭐</code></b> <b><code>&nbsp;&nbsp;2419🍴</code></b> [ruff](https://github.com/astral-sh/ruff)) - An extremely fast Python linter and code formatter.
  - <b><code>&nbsp;41845⭐</code></b> <b><code>&nbsp;&nbsp;2872🍴</code></b> [black](https://github.com/psf/black)) - The uncompromising Python code formatter.
  - <b><code>&nbsp;&nbsp;6953⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;686🍴</code></b> [isort](https://github.com/PyCQA/isort)) - A Python utility / library to sort imports.
  - <b><code>&nbsp;&nbsp;5725⭐</code></b> <b><code>&nbsp;&nbsp;1341🍴</code></b> [pylint](https://github.com/pylint-dev/pylint)) - A fully customizable source code analyzer.
  - <b><code>&nbsp;&nbsp;3823⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;356🍴</code></b> [flake8](https://github.com/PyCQA/flake8)) - A wrapper around `pycodestyle`, `pyflakes` and McCabe.
    - <b><code>&nbsp;&nbsp;1280⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;52🍴</code></b> [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions))
  - <b><code>&nbsp;&nbsp;8269⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;834🍴</code></b> [bandit](https://github.com/PyCQA/bandit)) - A tool designed to find common security issues in Python code.
- Refactoring
  - <b><code>&nbsp;&nbsp;2236⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;193🍴</code></b> [rope](https://github.com/python-rope/rope)) - Rope is a python refactoring library.
- Type Checkers - <b><code>&nbsp;&nbsp;1985⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;77🍴</code></b> [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing))
  - <b><code>&nbsp;20644⭐</code></b> <b><code>&nbsp;&nbsp;3303🍴</code></b> [mypy](https://github.com/python/mypy)) - Check variable types during compile time.
  - <b><code>&nbsp;19710⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;331🍴</code></b> [ty](https://github.com/astral-sh/ty)) - An extremely fast Python type checker and language server.
  - <b><code>&nbsp;15645⭐</code></b> <b><code>&nbsp;&nbsp;1816🍴</code></b> [pyright](https://github.com/microsoft/pyright)) - Full-featured static type checker for Python from Microsoft, the engine behind Pylance.
  - <b><code>&nbsp;&nbsp;6976⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;519🍴</code></b> [pyrefly](https://github.com/facebook/pyrefly)) - A fast type checker and language server for Python.
- Type Annotations Generators
  - <b><code>&nbsp;&nbsp;5002⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;209🍴</code></b> [monkeytype](https://github.com/Instagram/MonkeyType)) - A system for Python that generates static type annotations by collecting runtime types.

### Testing

_Libraries for testing codebases and generating test data. Also see <b><code>&nbsp;&nbsp;&nbsp;308⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;53🍴</code></b> [awesome-python-testing](https://github.com/cleder/awesome-python-testing))._

- Frameworks
  - <b><code>&nbsp;14513⭐</code></b> <b><code>&nbsp;&nbsp;3376🍴</code></b> [pytest](https://github.com/pytest-dev/pytest)) - A mature full-featured Python testing tool.
    - <b><code>&nbsp;&nbsp;&nbsp;575⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;67🍴</code></b> [awesome-pytest](https://github.com/augustogoulart/awesome-pytest))
  - <b><code>&nbsp;&nbsp;8978⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;673🍴</code></b> [hypothesis](https://github.com/HypothesisWorks/hypothesis)) - Hypothesis is an advanced Quickcheck style property based testing library.
  - <b><code>&nbsp;11895⭐</code></b> <b><code>&nbsp;&nbsp;2565🍴</code></b> [robotframework](https://github.com/robotframework/robotframework)) - A generic test automation framework.
- Test Runners
  - <b><code>&nbsp;&nbsp;3935⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;580🍴</code></b> [tox](https://github.com/tox-dev/tox)) - Auto builds and tests distributions in multiple Python versions
  - <b><code>&nbsp;&nbsp;1559⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;193🍴</code></b> [nox](https://github.com/wntrblm/nox)) - Flexible test automation for Python.
- Browser Automation
  - <b><code>&nbsp;15009⭐</code></b> <b><code>&nbsp;&nbsp;1225🍴</code></b> [playwright-python](https://github.com/microsoft/playwright-python)) - Python version of the Playwright testing and automation library.
  - <b><code>&nbsp;34496⭐</code></b> <b><code>&nbsp;&nbsp;8718🍴</code></b> [selenium](https://github.com/SeleniumHQ/selenium)) - Python bindings for 🌎 [Selenium](selenium.dev/) 🌎 [WebDriver](selenium.dev/documentation/webdriver/).
  - <b><code>&nbsp;13024⭐</code></b> <b><code>&nbsp;&nbsp;1583🍴</code></b> [seleniumbase](https://github.com/seleniumbase/SeleniumBase)) - Python framework for web automation & testing, with stealth options.
- Load Testing
  - <b><code>&nbsp;28166⭐</code></b> <b><code>&nbsp;&nbsp;3243🍴</code></b> [locust](https://github.com/locustio/locust)) - Scalable user load testing tool written in Python.
- API Testing
  - <b><code>&nbsp;&nbsp;3608⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;224🍴</code></b> [schemathesis](https://github.com/schemathesis/schemathesis)) - A tool for automatic property-based testing of web applications built with Open API / Swagger specifications.
- Mock
  - 🌎 [mock](docs.python.org/3/library/unittest.mock.html) - (Python standard library) A mocking and patching library.
  - <b><code>&nbsp;&nbsp;4343⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;378🍴</code></b> [responses](https://github.com/getsentry/responses)) - A utility library for mocking out the requests Python library.
  - <b><code>&nbsp;&nbsp;4525⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;305🍴</code></b> [freezegun](https://github.com/spulec/freezegun)) - Travel through time by mocking the datetime module.
  - <b><code>&nbsp;&nbsp;3009⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;441🍴</code></b> [vcrpy](https://github.com/kevin1024/vcrpy)) - Record and replay HTTP interactions on your tests.
  - <b><code>&nbsp;&nbsp;&nbsp;837⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;64🍴</code></b> [respx](https://github.com/lundberg/respx)) - Mock HTTPX with awesome request patterns and response side effects.
- Object Factories
  - <b><code>&nbsp;&nbsp;3806⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;421🍴</code></b> [factory_boy](https://github.com/FactoryBoy/factory_boy)) - A test fixtures replacement for Python.
  - <b><code>&nbsp;&nbsp;1508⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;120🍴</code></b> [polyfactory](https://github.com/litestar-org/polyfactory)) - mock data generation library with support to classes (continuation of `pydantic-factories`)
- Code Coverage
  - <b><code>&nbsp;&nbsp;3412⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;523🍴</code></b> [coverage](https://github.com/coveragepy/coveragepy)) - Code coverage measurement.
- Fake Data
  - <b><code>&nbsp;19403⭐</code></b> <b><code>&nbsp;&nbsp;2115🍴</code></b> [faker](https://github.com/joke2k/faker)) - A Python package that generates fake data.
  - <b><code>&nbsp;&nbsp;4843⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;361🍴</code></b> [mimesis](https://github.com/lk-geimfari/mimesis)) - is a Python library that help you generate fake data.

### Debugging Tools

_Libraries for debugging code._

- pdb-like Debugger
  - <b><code>&nbsp;&nbsp;1974⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;152🍴</code></b> [ipdb](https://github.com/gotcha/ipdb)) - IPython-enabled 🌎 [pdb](docs.python.org/3/library/pdb.html).
  - <b><code>&nbsp;&nbsp;3247⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;245🍴</code></b> [pudb](https://github.com/inducer/pudb)) - A full-screen, console-based Python debugger.
- Tracing
  - <b><code>&nbsp;&nbsp;&nbsp;872⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51🍴</code></b> [hunter](https://github.com/ionelmc/python-hunter)) - A flexible code tracing toolkit.
- Profiler
  - <b><code>&nbsp;15504⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;546🍴</code></b> [py-spy](https://github.com/benfred/py-spy)) - A sampling profiler for Python programs. Written in Rust.
  - <b><code>&nbsp;15236⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;463🍴</code></b> [memray](https://github.com/bloomberg/memray)) - A memory profiler that tracks allocations in Python code, native extensions, and the interpreter itself.
  - <b><code>&nbsp;&nbsp;8006⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;301🍴</code></b> [pyinstrument](https://github.com/joerick/pyinstrument)) - A statistical wall-clock profiler with low overhead and readable call-tree output.
  - <b><code>&nbsp;13509⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;437🍴</code></b> [scalene](https://github.com/plasma-umass/scalene)) - A high-performance, high-precision CPU, GPU, and memory profiler for Python.
- Others
  - <b><code>&nbsp;&nbsp;8381⭐</code></b> <b><code>&nbsp;&nbsp;1105🍴</code></b> [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar)) - Display various debug information for Django.
  - <b><code>&nbsp;10109⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;232🍴</code></b> [icecream](https://github.com/gruns/icecream)) - Inspect variables, expressions, and program execution with a single, simple function call.
  - <b><code>&nbsp;&nbsp;&nbsp;978⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar)) - A port of the django-debug-toolbar to flask.

### Build Tools

_Compile software from source code. If you're looking for Python packaging/build tools, see [Package Management](#package-management)._

- <b><code>&nbsp;&nbsp;4777⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;410🍴</code></b> [invoke](https://github.com/pyinvoke/invoke)) - A tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks.
- <b><code>&nbsp;&nbsp;2419⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;360🍴</code></b> [scons](https://github.com/SCons/scons)) - A software construction tool.
- <b><code>&nbsp;&nbsp;2084⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;195🍴</code></b> [doit](https://github.com/pydoit/doit)) - A task runner and build tool.

### Documentation

_Libraries for generating project documentation._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [sphinx](https://github.com/sphinx-doc/sphinx/)) - Python Documentation generator.
  - <b><code>&nbsp;&nbsp;&nbsp;979⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;78🍴</code></b> [awesome-sphinxdoc](https://github.com/ygzgxyz/awesome-sphinxdoc))
- <b><code>&nbsp;27456⭐</code></b> <b><code>&nbsp;&nbsp;4148🍴</code></b> [mkdocs-material](https://github.com/squidfunk/mkdocs-material)) - A documentation framework and Material Design theme built on MkDocs.
- <b><code>&nbsp;42621⭐</code></b> <b><code>&nbsp;&nbsp;2733🍴</code></b> [diagrams](https://github.com/mingrammer/diagrams)) - Diagram as Code.
- <b><code>&nbsp;&nbsp;2512⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;228🍴</code></b> [pdoc](https://github.com/mitmproxy/pdoc)) - Epydoc replacement to auto generate API documentation for Python libraries.
- <b><code>&nbsp;&nbsp;5729⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;131🍴</code></b> [zensical](https://github.com/zensical/zensical)) - A modern static site generator for technical documentation.

**DevOps**

### DevOps Tools

_Software and libraries for DevOps._

- Cloud Providers
  - <b><code>&nbsp;&nbsp;9904⭐</code></b> <b><code>&nbsp;&nbsp;1995🍴</code></b> [boto3](https://github.com/boto/boto3)) - Python interface to Amazon Web Services.
  - <b><code>&nbsp;17265⭐</code></b> <b><code>&nbsp;&nbsp;4651🍴</code></b> [awscli](https://github.com/aws/aws-cli)) - Universal Command Line Interface for Amazon Web Services.
  - <b><code>&nbsp;&nbsp;5600⭐</code></b> <b><code>&nbsp;&nbsp;3367🍴</code></b> [azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python)) - Microsoft Azure SDK for Python, published as per-service packages.
  - <b><code>&nbsp;&nbsp;5385⭐</code></b> <b><code>&nbsp;&nbsp;1769🍴</code></b> [google-cloud-python](https://github.com/googleapis/google-cloud-python)) - Google Cloud client libraries for Python, published as per-service packages.
- Configuration Management
  - <b><code>&nbsp;70716⭐</code></b> <b><code>&nbsp;24335🍴</code></b> [ansible](https://github.com/ansible/ansible)) - A radically simple IT automation platform.
  - <b><code>&nbsp;&nbsp;3815⭐</code></b> <b><code>&nbsp;&nbsp;1139🍴</code></b> [cloud-init](https://github.com/canonical/cloud-init)) - A multi-distribution package that handles early initialization of a cloud instance.
  - <b><code>&nbsp;&nbsp;6000⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;547🍴</code></b> [pyinfra](https://github.com/pyinfra-dev/pyinfra)) - A versatile CLI tools and python libraries to automate infrastructure.
  - <b><code>&nbsp;15661⭐</code></b> <b><code>&nbsp;&nbsp;5610🍴</code></b> [salt](https://github.com/saltstack/salt)) - Infrastructure automation and management system.
- Deployment
  - <b><code>&nbsp;15503⭐</code></b> <b><code>&nbsp;&nbsp;1952🍴</code></b> [fabric](https://github.com/fabric/fabric)) - A simple, Pythonic tool for remote execution and deployment.
  - <b><code>&nbsp;11059⭐</code></b> <b><code>&nbsp;&nbsp;1011🍴</code></b> [chalice](https://github.com/aws/chalice)) - A Python serverless microframework for AWS.
- Monitoring and Processes
  - <b><code>&nbsp;11277⭐</code></b> <b><code>&nbsp;&nbsp;1514🍴</code></b> [psutil](https://github.com/giampaolo/psutil)) - A cross-platform process and system utilities module.
  - <b><code>&nbsp;&nbsp;2204⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;671🍴</code></b> [sentry-sdk](https://github.com/getsentry/sentry-python)) - Sentry SDK for Python.
  - <b><code>&nbsp;&nbsp;9116⭐</code></b> <b><code>&nbsp;&nbsp;1269🍴</code></b> [supervisor](https://github.com/Supervisor/supervisor)) - Supervisor process control system for UNIX.
  - <b><code>&nbsp;&nbsp;7238⭐</code></b> <b><code>&nbsp;&nbsp;1155🍴</code></b> [flower](https://github.com/mher/flower)) - A real-time monitor and web admin for Celery task queues.
  - <b><code>&nbsp;&nbsp;7241⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;505🍴</code></b> [sh](https://github.com/amoffat/sh)) - A full-fledged subprocess replacement for Python.
- Other
  - <b><code>&nbsp;13733⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;876🍴</code></b> [borgbackup](https://github.com/borgbackup/borg)) - A deduplicating archiver with compression and encryption.
  - <b><code>&nbsp;&nbsp;2027⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;206🍴</code></b> [chaostoolkit](https://github.com/chaostoolkit/chaostoolkit)) - A Chaos Engineering toolkit & Orchestration for Developers.

### Distributed Computing

_Frameworks and libraries for Distributed Computing._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [ray](https://github.com/ray-project/ray/)) - A system for parallel and distributed Python that unifies the machine learning ecosystem.
- <b><code>&nbsp;44007⭐</code></b> <b><code>&nbsp;29384🍴</code></b> [pyspark](https://github.com/apache/spark)) - 🌎 [Apache Spark](spark.apache.org/) Python API.
- <b><code>&nbsp;13921⭐</code></b> <b><code>&nbsp;&nbsp;1956🍴</code></b> [dask](https://github.com/dask/dask)) - A flexible parallel computing library for analytic computing.
- <b><code>&nbsp;&nbsp;4394⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;480🍴</code></b> [joblib](https://github.com/joblib/joblib)) - A set of tools to provide lightweight pipelining in Python.
- <b><code>&nbsp;&nbsp;&nbsp;923⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;136🍴</code></b> [mpi4py](https://github.com/mpi4py/mpi4py)) - Python bindings for MPI.

### Task Queues

_Libraries for working with task queues._

- <b><code>&nbsp;28898⭐</code></b> <b><code>&nbsp;&nbsp;5168🍴</code></b> [celery](https://github.com/celery/celery)) - An asynchronous task queue/job queue based on distributed message passing.
- <b><code>&nbsp;10687⭐</code></b> <b><code>&nbsp;&nbsp;1497🍴</code></b> [rq](https://github.com/rq/rq)) - Simple job queues for Python.
- <b><code>&nbsp;&nbsp;5311⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;383🍴</code></b> [dramatiq](https://github.com/Bogdanp/dramatiq)) - A fast and reliable background task processing library for Python 3.
- <b><code>&nbsp;&nbsp;6034⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;403🍴</code></b> [huey](https://github.com/coleifer/huey)) - Little multi-threaded task queue.
- <b><code>&nbsp;&nbsp;2335⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;143🍴</code></b> [taskiq](https://github.com/taskiq-python/taskiq)) - Distributed task queue with native asyncio support and pluggable brokers.

### Messaging

_Libraries for working with message brokers and event streaming._

- <b><code>&nbsp;&nbsp;&nbsp;509⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;965🍴</code></b> [confluent-kafka](https://github.com/confluentinc/confluent-kafka-python)) - Confluent's Python client for Apache Kafka, built on librdkafka.
- <b><code>&nbsp;&nbsp;3885⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;856🍴</code></b> [pika](https://github.com/pika/pika)) - Pure-Python RabbitMQ/AMQP 0-9-1 client library.
- <b><code>&nbsp;&nbsp;2422⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;743🍴</code></b> [paho-mqtt](https://github.com/eclipse-paho/paho.mqtt.python)) - The Eclipse Paho MQTT client for Python.
- <b><code>&nbsp;&nbsp;5343⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;394🍴</code></b> [faststream](https://github.com/ag2ai/faststream)) - A framework for building asynchronous services over Apache Kafka, RabbitMQ, NATS, MQTT and Redis.

### Job Schedulers

_Libraries for scheduling jobs._

- Task Scheduling
  - <b><code>&nbsp;&nbsp;7630⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;784🍴</code></b> [apscheduler](https://github.com/agronholm/apscheduler)) - A light but powerful in-process task scheduler that lets you schedule functions.
  - <b><code>&nbsp;12267⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;999🍴</code></b> [schedule](https://github.com/dbader/schedule)) - Python job scheduling for humans.
- Workflow Orchestration
  - <b><code>&nbsp;46884⭐</code></b> <b><code>&nbsp;17861🍴</code></b> [apache-airflow](https://github.com/apache/airflow)) - Airflow is a platform to programmatically author, schedule and monitor workflows.
  - <b><code>&nbsp;23859⭐</code></b> <b><code>&nbsp;&nbsp;2528🍴</code></b> [prefect](https://github.com/PrefectHQ/prefect)) - A modern workflow orchestration framework that makes it easy to build, schedule and monitor robust data pipelines.
  - <b><code>&nbsp;16168⭐</code></b> <b><code>&nbsp;&nbsp;2294🍴</code></b> [dagster](https://github.com/dagster-io/dagster)) - An orchestration platform for the development, production, and observation of data assets.

### Logging

_Libraries for generating and working with logs._

- 🌎 [logging](docs.python.org/3/library/logging.html) - (Python standard library) Logging facility for Python.
- <b><code>&nbsp;&nbsp;4953⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;298🍴</code></b> [structlog](https://github.com/hynek/structlog)) - Structured logging made easy.
- <b><code>&nbsp;24114⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;816🍴</code></b> [loguru](https://github.com/Delgan/loguru)) - Library which aims to bring enjoyable logging in Python.

### Network Virtualization

_Tools and libraries for Virtual Networking and SDN (Software Defined Networking)._

- <b><code>&nbsp;12549⭐</code></b> <b><code>&nbsp;&nbsp;2246🍴</code></b> [scapy](https://github.com/secdev/scapy)) - A brilliant packet manipulation library.
- <b><code>&nbsp;&nbsp;2502⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;592🍴</code></b> [napalm](https://github.com/napalm-automation/napalm)) - Cross-vendor API to manipulate network devices.

**CLI & GUI**

### CLI Development

_Libraries for building command-line applications._

- CLI Development
  - 🌎 [argparse](docs.python.org/3/library/argparse.html) - (Python standard library) Command-line option and argument parsing.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [click](https://github.com/pallets/click/)) - A package for creating beautiful command line interfaces in a composable way.
  - <b><code>&nbsp;19993⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;979🍴</code></b> [typer](https://github.com/fastapi/typer)) - Modern CLI framework that uses Python type hints. Built on Click and Pydantic.
  - <b><code>&nbsp;10575⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;813🍴</code></b> [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)) - A library for building powerful interactive command lines.
  - <b><code>&nbsp;28225⭐</code></b> <b><code>&nbsp;&nbsp;1493🍴</code></b> [fire](https://github.com/google/python-fire)) - A library for creating command line interfaces from absolutely any Python object.
- Terminal Rendering
  - <b><code>&nbsp;31338⭐</code></b> <b><code>&nbsp;&nbsp;1648🍴</code></b> [tqdm](https://github.com/tqdm/tqdm)) - Fast, extensible progress bar for loops and CLI.
  - <b><code>&nbsp;57384⭐</code></b> <b><code>&nbsp;&nbsp;2354🍴</code></b> [rich](https://github.com/Textualize/rich)) - Python library for rich text and beautiful formatting in the terminal. Also provides a great `RichHandler` log handler.
  - <b><code>&nbsp;&nbsp;3795⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;283🍴</code></b> [colorama](https://github.com/tartley/colorama)) - Cross-platform colored terminal text.
  - <b><code>&nbsp;&nbsp;6307⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;236🍴</code></b> [alive-progress](https://github.com/rsalmei/alive-progress)) - A new kind of Progress Bar, with real-time throughput, eta and very cool animations.
- TUI Frameworks
  - <b><code>&nbsp;37266⭐</code></b> <b><code>&nbsp;&nbsp;1336🍴</code></b> [textual](https://github.com/Textualize/textual)) - A framework for building interactive user interfaces that run in the terminal and the browser.
  - <b><code>&nbsp;&nbsp;3020⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;343🍴</code></b> [urwid](https://github.com/urwid/urwid)) - A library for creating terminal GUI applications with strong support for widgets, events, rich colors, etc.
  - <b><code>&nbsp;&nbsp;4303⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;264🍴</code></b> [asciimatics](https://github.com/peterbrittain/asciimatics)) - A package to create full-screen text UIs (from interactive forms to ASCII animations).

### CLI Tools

_Useful CLI-based tools._

- Database CLIs
  - <b><code>&nbsp;13392⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;613🍴</code></b> [pgcli](https://github.com/dbcli/pgcli)) - PostgreSQL CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;11977⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;699🍴</code></b> [mycli](https://github.com/dbcli/mycli)) - MySQL CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;&nbsp;3300⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;95🍴</code></b> [litecli](https://github.com/dbcli/litecli)) - SQLite CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;&nbsp;2744⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;120🍴</code></b> [iredis](https://github.com/laixintao/iredis)) - Redis CLI with autocompletion and syntax highlighting.
- Downloaders
  - <b><code>191802⭐</code></b> <b><code>&nbsp;16650🍴</code></b> [yt-dlp](https://github.com/yt-dlp/yt-dlp)) - A command-line program to download videos from YouTube and other video sites, a fork of youtube-dl.
- HTTP Clients
  - <b><code>&nbsp;38524⭐</code></b> <b><code>&nbsp;&nbsp;4004🍴</code></b> [httpie](https://github.com/httpie/cli)) - A command line HTTP client, a user-friendly cURL replacement.
- Project Scaffolding
  - <b><code>&nbsp;25091⭐</code></b> <b><code>&nbsp;&nbsp;2277🍴</code></b> [cookiecutter](https://github.com/cookiecutter/cookiecutter)) - A command-line utility that creates projects from cookiecutters (project templates).
  - <b><code>&nbsp;&nbsp;3579⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;273🍴</code></b> [copier](https://github.com/copier-org/copier)) - A library and command-line utility for rendering projects templates.
- Shells
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [xonsh](https://github.com/xonsh/xonsh/)) - A Python-powered shell. Full-featured and cross-platform.
- Terminal Workflow
  - <b><code>&nbsp;&nbsp;4582⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;248🍴</code></b> [tmuxp](https://github.com/tmux-python/tmuxp)) - A <b><code>&nbsp;49317⭐</code></b> <b><code>&nbsp;&nbsp;2893🍴</code></b> [tmux](https://github.com/tmux/tmux)) session manager.

### GUI Development

_Libraries for working with graphical user interface applications._

- Desktop
  - <b><code>&nbsp;&nbsp;&nbsp;159⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30🍴</code></b> [pygobject](https://github.com/GNOME/pygobject)) - Python Bindings for GLib/GObject/GIO/GTK+ (GTK+3).
  - <b><code>&nbsp;&nbsp;2625⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;565🍴</code></b> [wxPython](https://github.com/wxWidgets/Phoenix)) - A blending of the wxWidgets C++ class library with the Python.
  - <b><code>&nbsp;19018⭐</code></b> <b><code>&nbsp;&nbsp;3138🍴</code></b> [kivy](https://github.com/kivy/kivy)) - A library for creating NUI applications, running on Windows, Linux, Mac OS X, Android and iOS.
  - <b><code>&nbsp;15623⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;783🍴</code></b> [dearpygui](https://github.com/hoffstadt/DearPyGui)) - A Simple GPU accelerated Python GUI framework
  - <b><code>&nbsp;&nbsp;5414⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;828🍴</code></b> [toga](https://github.com/beeware/toga)) - A Python native, OS native GUI toolkit.
- Qt
  - <b><code>&nbsp;&nbsp;&nbsp;133⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;32🍴</code></b> [PySide6](https://github.com/pyside/pyside-setup)) - Qt for Python offers the official Python bindings for 🌎 [Qt](www.qt.io/), same as PyQt6 but it's the official binding with different licensing.
  - 🌎 [PyQt6](www.riverbankcomputing.com/static/Docs/PyQt6/) - Python bindings for the 🌎 [Qt](www.qt.io/) cross-platform application and UI framework.
- Tkinter
  - 🌎 [tkinter](docs.python.org/3/library/tkinter.html) - (Python standard library) The standard Python interface to the Tcl/Tk GUI toolkit.
  - <b><code>&nbsp;13553⭐</code></b> <b><code>&nbsp;&nbsp;1159🍴</code></b> [customtkinter](https://github.com/tomschimansky/customtkinter)) - A modern and customizable python UI-library based on Tkinter.
  - <b><code>&nbsp;10264⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;930🍴</code></b> [tkdesigner](https://github.com/ParthJadhav/Tkinter-Designer)) - Generates Tkinter interfaces from Figma designs using the Figma API.
- Web-based
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [pywebview](https://github.com/r0x0r/pywebview/)) - A lightweight cross-platform native wrapper around a webview component.
  - <b><code>&nbsp;16213⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;947🍴</code></b> [nicegui](https://github.com/zauberzeug/nicegui)) - An easy-to-use, Python-based UI framework, which shows up in your web browser.
  - <b><code>&nbsp;16847⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;694🍴</code></b> [flet](https://github.com/flet-dev/flet)) - Cross-platform GUI framework for building modern apps in pure Python.
- Wrappers
  - <b><code>&nbsp;21904⭐</code></b> <b><code>&nbsp;&nbsp;1042🍴</code></b> [gooey](https://github.com/chriskiehl/Gooey)) - Turn command line programs into a full GUI application with one line.

**Text & Documents**

### Text Processing

_Libraries for parsing and manipulating plain texts._

- Encoding and Unicode
  - <b><code>&nbsp;&nbsp;&nbsp;795⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;68🍴</code></b> [charset-normalizer](https://github.com/jawah/charset_normalizer)) - Universal character encoding detector, the default of the requests ecosystem.
  - <b><code>&nbsp;&nbsp;2667⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;305🍴</code></b> [chardet](https://github.com/chardet/chardet)) - Python character encoding detector.
  - <b><code>&nbsp;&nbsp;4063⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;128🍴</code></b> [ftfy](https://github.com/rspeer/python-ftfy)) - Makes Unicode text less broken and more consistent automagically.
- Fuzzy Matching
  - <b><code>&nbsp;&nbsp;4129⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;173🍴</code></b> [rapidfuzz](https://github.com/rapidfuzz/RapidFuzz)) - Rapid fuzzy string matching using various string metrics, with a C++ core.
- General
  - 🌎 [difflib](docs.python.org/3/library/difflib.html) - (Python standard library) Helpers for computing deltas.
  - <b><code>&nbsp;&nbsp;1582⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;158🍴</code></b> [pyfiglet](https://github.com/pwaller/pyfiglet)) - An implementation of figlet written in Python.
- Internationalization
  - <b><code>&nbsp;&nbsp;1466⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;503🍴</code></b> [babel](https://github.com/python-babel/babel)) - An internationalization library for Python.
- Parser
  - <b><code>&nbsp;&nbsp;2207⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;884🍴</code></b> [pygments](https://github.com/pygments/pygments)) - A generic syntax highlighter.
  - <b><code>&nbsp;&nbsp;2490⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;335🍴</code></b> [pyparsing](https://github.com/pyparsing/pyparsing)) - A general purpose framework for generating parsers.
  - <b><code>&nbsp;&nbsp;4017⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;747🍴</code></b> [sqlparse](https://github.com/andialbrecht/sqlparse)) - A non-validating SQL parser.
  - <b><code>&nbsp;&nbsp;3773⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;442🍴</code></b> [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)) - Parsing, formatting, storing and validating international phone numbers.
  - <b><code>&nbsp;&nbsp;&nbsp;452⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;45🍴</code></b> [parsy](https://github.com/python-parsy/parsy)) - Easy, generic parser combinator library for creating parsers.
- Transliteration and Slugs
  - <b><code>&nbsp;&nbsp;1624⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;139🍴</code></b> [python-slugify](https://github.com/un33k/python-slugify)) - A Python slugify library that translates unicode to ASCII.
  - <b><code>&nbsp;&nbsp;&nbsp;609⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;65🍴</code></b> [unidecode](https://github.com/avian2/unidecode)) - ASCII transliterations of Unicode text.
- Unique identifiers
  - <b><code>&nbsp;&nbsp;2200⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [shortuuid](https://github.com/skorokithakis/shortuuid)) - A generator library for concise, unambiguous and URL-safe UUIDs.
  - <b><code>&nbsp;&nbsp;&nbsp;524⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;12🍴</code></b> [sqids](https://github.com/sqids/sqids-python)) - A library for generating short unique IDs from numbers.

### HTML Manipulation

_Libraries for working with HTML and XML._

- 🌎 [beautifulsoup4](www.crummy.com/software/BeautifulSoup/bs4/doc/) - Providing Pythonic idioms for iterating, searching, and modifying HTML or XML.
- <b><code>&nbsp;&nbsp;3056⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;640🍴</code></b> [lxml](https://github.com/lxml/lxml)) - A very fast, easy-to-use and versatile library for handling HTML and XML.
- <b><code>&nbsp;&nbsp;5756⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;475🍴</code></b> [xmltodict](https://github.com/martinblech/xmltodict)) - Working with XML feel like you are working with JSON.
- <b><code>&nbsp;&nbsp;&nbsp;697⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;184🍴</code></b> [markupsafe](https://github.com/pallets/markupsafe)) - Implements a XML/HTML/XHTML Markup safe string for Python.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [justhtml](https://github.com/EmilStenstrom/justhtml/)) - A pure Python HTML5 parser that just works.

### File Format Processing

_Libraries for parsing and manipulating specific text formats._

- General
  - <b><code>&nbsp;&nbsp;2281⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;547🍴</code></b> [pyelftools](https://github.com/eliben/pyelftools)) - Parsing and analyzing ELF files and DWARF debugging information.
  - <b><code>&nbsp;&nbsp;4757⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;617🍴</code></b> [tablib](https://github.com/jazzband/tablib)) - A module for Tabular Datasets in XLS, CSV, JSON, YAML.
- File Conversion
  - <b><code>185164⭐</code></b> <b><code>&nbsp;13634🍴</code></b> [markitdown](https://github.com/microsoft/markitdown)) - Python tool for converting files and office documents to Markdown.
  - <b><code>&nbsp;66581⭐</code></b> <b><code>&nbsp;&nbsp;4800🍴</code></b> [docling](https://github.com/docling-project/docling)) - Library for converting documents into structured data.
- Excel
  - 🌎 [openpyxl](openpyxl.readthedocs.io/en/stable/) - A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.
  - <b><code>&nbsp;&nbsp;3972⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;671🍴</code></b> [xlsxwriter](https://github.com/jmcnamara/XlsxWriter)) - A Python module for creating Excel .xlsx files.
- Word
  - <b><code>&nbsp;&nbsp;5722⭐</code></b> <b><code>&nbsp;&nbsp;1309🍴</code></b> [python-docx](https://github.com/python-openxml/python-docx)) - Reads, queries and modifies Microsoft Word 2007/2008 docx files.
- PowerPoint
  - <b><code>&nbsp;&nbsp;3534⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;737🍴</code></b> [python-pptx](https://github.com/scanny/python-pptx)) - Python library for creating and updating PowerPoint (.pptx) files.
- PDF
  - <b><code>&nbsp;10207⭐</code></b> <b><code>&nbsp;&nbsp;1627🍴</code></b> [pypdf](https://github.com/py-pdf/pypdf)) - A library capable of splitting, merging, cropping, and transforming PDF pages.
  - 🌎 [reportlab](www.reportlab.com/opensource/) - Allowing Rapid creation of rich PDF documents.
  - <b><code>&nbsp;&nbsp;7025⭐</code></b> <b><code>&nbsp;&nbsp;1040🍴</code></b> [pdfminer.six](https://github.com/pdfminer/pdfminer.six)) - Pdfminer.six is a community maintained fork of the original PDFMiner.
- HTML-to-PDF
  - <b><code>&nbsp;&nbsp;9608⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;877🍴</code></b> [weasyprint](https://github.com/Kozea/WeasyPrint)) - A visual rendering engine for HTML and CSS that can export to PDF.
- Markdown
  - <b><code>&nbsp;&nbsp;1364⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;122🍴</code></b> [markdown-it-py](https://github.com/executablebooks/markdown-it-py)) - Markdown parser with 100% CommonMark support, extensions, and syntax plugins.
  - <b><code>&nbsp;&nbsp;4248⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;904🍴</code></b> [markdown](https://github.com/Python-Markdown/markdown)) - A Python implementation of John Gruber’s Markdown.
  - <b><code>&nbsp;&nbsp;3075⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;302🍴</code></b> [mistune](https://github.com/lepture/mistune)) - Fastest and full featured pure Python parsers of Markdown.
- Data Formats
  - 🌎 [tomllib](docs.python.org/3/library/tomllib.html) - (Python standard library) Parse TOML files.
  - <b><code>&nbsp;&nbsp;2945⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;607🍴</code></b> [pyyaml](https://github.com/yaml/pyyaml)) - YAML implementations for Python.

### File Manipulation

_Libraries for file manipulation._

- 🌎 [mimetypes](docs.python.org/3/library/mimetypes.html) - (Python standard library) Map filenames to MIME types.
- 🌎 [pathlib](docs.python.org/3/library/pathlib.html) - (Python standard library) A cross-platform, object-oriented path library.
- <b><code>&nbsp;&nbsp;2536⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;146🍴</code></b> [watchfiles](https://github.com/samuelcolvin/watchfiles)) - Simple, modern and fast file watching and code reload in python.
- <b><code>&nbsp;&nbsp;7416⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;788🍴</code></b> [watchdog](https://github.com/gorakhargosh/watchdog)) - API and shell utilities to monitor file system events.
- <b><code>&nbsp;&nbsp;2918⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;304🍴</code></b> [python-magic](https://github.com/ahupp/python-magic)) - A Python interface to the libmagic file type identification library.

**Media**

### Image Processing

_Libraries for manipulating images._

- Barcodes and QR Codes
  - <b><code>&nbsp;&nbsp;4938⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;745🍴</code></b> [qrcode](https://github.com/lincolnloop/python-qrcode)) - A pure Python QR Code generator.
  - <b><code>&nbsp;&nbsp;&nbsp;655⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;137🍴</code></b> [python-barcode](https://github.com/WhyNotHugo/python-barcode)) - Create barcodes in Python with no extra dependencies.
- General
  - <b><code>&nbsp;13821⭐</code></b> <b><code>&nbsp;&nbsp;2507🍴</code></b> [pillow](https://github.com/python-pillow/Pillow)) - Pillow is the friendly 🌎 [PIL](www.pythonware.com/products/pil/) fork.
  - <b><code>&nbsp;&nbsp;6591⭐</code></b> <b><code>&nbsp;&nbsp;2408🍴</code></b> [scikit-image](https://github.com/scikit-image/scikit-image)) - A Python library for (scientific) image processing.
  - <b><code>&nbsp;24785⭐</code></b> <b><code>&nbsp;&nbsp;2423🍴</code></b> [rembg](https://github.com/danielgatis/rembg)) - A tool to remove image backgrounds.
  - <b><code>&nbsp;&nbsp;1479⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;202🍴</code></b> [wand](https://github.com/emcconville/wand)) - Python bindings for 🌎 [MagickWand](www.imagemagick.org/script/magick-wand.php), C API for ImageMagick.
  - <b><code>&nbsp;&nbsp;&nbsp;812⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63🍴</code></b> [pyvips](https://github.com/libvips/pyvips)) - A fast image processing library with low memory needs.
- Image Serving
  - <b><code>&nbsp;10518⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;862🍴</code></b> [thumbor](https://github.com/thumbor/thumbor)) - A smart imaging service. It enables on-demand crop, re-sizing and flipping of images.

### Audio & Video Processing

_Libraries for manipulating audio, video, and their metadata._

- Audio
  - <b><code>&nbsp;&nbsp;9793⭐</code></b> <b><code>&nbsp;&nbsp;1135🍴</code></b> [pydub](https://github.com/jiaaro/pydub)) - Manipulate audio with a simple and easy high level interface.
  - <b><code>&nbsp;&nbsp;8615⭐</code></b> <b><code>&nbsp;&nbsp;1075🍴</code></b> [librosa](https://github.com/librosa/librosa)) - Python library for audio and music analysis.
- Video
  - <b><code>&nbsp;14901⭐</code></b> <b><code>&nbsp;&nbsp;2106🍴</code></b> [moviepy](https://github.com/Zulko/moviepy)) - A module for script-based movie editing with many formats, including animated GIFs.
  - <b><code>&nbsp;&nbsp;3722⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;286🍴</code></b> [vidgear](https://github.com/abhiTronix/vidgear)) - Most Powerful multi-threaded Video Processing framework.
- Metadata
  - <b><code>&nbsp;&nbsp;1957⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;196🍴</code></b> [mutagen](https://github.com/quodlibet/mutagen)) - A Python module to handle audio metadata.
  - <b><code>&nbsp;&nbsp;&nbsp;840⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;105🍴</code></b> [tinytag](https://github.com/tinytag/tinytag)) - A library for reading music meta data of MP3, OGG, FLAC and Wave files.
  - <b><code>&nbsp;15672⭐</code></b> <b><code>&nbsp;&nbsp;2114🍴</code></b> [beets](https://github.com/beetbox/beets)) - A music library manager and 🌎 [MusicBrainz](musicbrainz.org/) tagger.

### Game Development

_Awesome game development libraries._

- 3D Engines
  - <b><code>&nbsp;&nbsp;5225⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;891🍴</code></b> [panda3d](https://github.com/panda3d/panda3d)) - 3D game engine developed by Disney.
- Game Frameworks
  - <b><code>&nbsp;&nbsp;8940⭐</code></b> <b><code>&nbsp;&nbsp;4209🍴</code></b> [pygame](https://github.com/pygame/pygame)) - Pygame is a set of Python modules designed for writing games.
  - <b><code>&nbsp;&nbsp;2214⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;340🍴</code></b> [pyglet](https://github.com/pyglet/pyglet)) - A cross-platform windowing and multimedia library for Python.
  - <b><code>&nbsp;&nbsp;1653⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;281🍴</code></b> [pygame-ce](https://github.com/pygame-community/pygame-ce)) - An actively developed drop-in replacement with new features and performance improvements (<b><code>&nbsp;&nbsp;8940⭐</code></b> <b><code>&nbsp;&nbsp;4209🍴</code></b> [pygame](https://github.com/pygame/pygame)) fork).
  - <b><code>&nbsp;&nbsp;2078⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;381🍴</code></b> [arcade](https://github.com/pythonarcade/arcade)) - Arcade is a modern Python framework for crafting games with compelling graphics and sound.
- Visual Novels
  - <b><code>&nbsp;&nbsp;6833⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;936🍴</code></b> [renpy](https://github.com/renpy/renpy)) - A Visual Novel engine.

**Python Language**

### Implementations

_Implementations of Python._

- <b><code>&nbsp;77205⭐</code></b> <b><code>&nbsp;35741🍴</code></b> [cpython](https://github.com/python/cpython)) - Default, most widely used implementation of the Python programming language written in C.
- <b><code>&nbsp;22071⭐</code></b> <b><code>&nbsp;&nbsp;8974🍴</code></b> [micropython](https://github.com/micropython/micropython)) - A lean and efficient Python programming language implementation.
- <b><code>&nbsp;&nbsp;1795⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;125🍴</code></b> [pypy](https://github.com/pypy/pypy)) - A very fast and compliant implementation of the Python language.
- <b><code>&nbsp;10844⭐</code></b> <b><code>&nbsp;&nbsp;1624🍴</code></b> [Cython](https://github.com/cython/cython)) - Optimizing Static Compiler for Python.
- <b><code>&nbsp;14835⭐</code></b> <b><code>&nbsp;&nbsp;1045🍴</code></b> [pyodide](https://github.com/pyodide/pyodide)) - Python distribution for the browser and Node.js based on WebAssembly.

### Built-in Classes Enhancement

_Libraries for enhancing Python built-in classes._

- <b><code>&nbsp;&nbsp;5841⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;480🍴</code></b> [attrs](https://github.com/python-attrs/attrs)) - Replacement for `__init__`, `__eq__`, `__repr__`, etc. boilerplate in class definitions.
- <b><code>&nbsp;&nbsp;1587⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;68🍴</code></b> [bidict](https://github.com/jab/bidict)) - Efficient, Pythonic bidirectional map data structures and related functionality.
- <b><code>&nbsp;&nbsp;&nbsp;373⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;21🍴</code></b> [uuid-utils](https://github.com/aminalaee/uuid-utils)) - A fast, Rust-backed drop-in replacement for Python's built-in `uuid` module, supporting RFC 9562 (UUIDv6, UUIDv7, and UUIDv8).
- <b><code>&nbsp;&nbsp;2832⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;135🍴</code></b> [python-box](https://github.com/cdgriffith/Box)) - Python dictionaries with advanced dot notation access.

### Functional Programming

_Functional Programming with Python._

- 🌎 [functools](docs.python.org/3/library/functools.html) - (Python standard library) Higher-order functions and operations on callable objects.
- <b><code>&nbsp;&nbsp;4092⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;368🍴</code></b> [more-itertools](https://github.com/more-itertools/more-itertools)) - More routines for operating on iterables, beyond `itertools`.
- <b><code>&nbsp;&nbsp;5157⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;279🍴</code></b> [toolz](https://github.com/pytoolz/toolz)) - A collection of functional utilities for iterators, functions, and dictionaries. Also available as <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [cytoolz](https://github.com/pytoolz/cytoolz/)) for Cython-accelerated performance.
- <b><code>&nbsp;&nbsp;3510⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;161🍴</code></b> [funcy](https://github.com/Suor/funcy)) - A fancy and practical functional tools.
- <b><code>&nbsp;&nbsp;4365⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;154🍴</code></b> [returns](https://github.com/dry-python/returns)) - A set of type-safe monads, transformers, and composition utilities.

### Asynchronous Programming

_Libraries for asynchronous, concurrent and parallel execution. Also see <b><code>&nbsp;&nbsp;5129⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;355🍴</code></b> [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio))._

- Async I/O
  - 🌎 [asyncio](docs.python.org/3/library/asyncio.html) - (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
    - <b><code>&nbsp;&nbsp;5129⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;355🍴</code></b> [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio))
  - <b><code>&nbsp;&nbsp;2544⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;265🍴</code></b> [anyio](https://github.com/agronholm/anyio)) - A high-level async concurrency and networking framework that works on top of asyncio or trio.
  - <b><code>&nbsp;11896⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;616🍴</code></b> [uvloop](https://github.com/MagicStack/uvloop)) - Ultra fast asyncio event loop.
  - <b><code>&nbsp;&nbsp;7331⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;431🍴</code></b> [trio](https://github.com/python-trio/trio)) - A friendly library for async concurrency and I/O.
  - <b><code>&nbsp;&nbsp;6447⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;967🍴</code></b> [gevent](https://github.com/gevent/gevent)) - A coroutine-based Python networking library that uses <b><code>&nbsp;&nbsp;1850⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;270🍴</code></b> [greenlet](https://github.com/python-greenlet/greenlet)).
  - <b><code>&nbsp;&nbsp;5982⭐</code></b> <b><code>&nbsp;&nbsp;1223🍴</code></b> [Twisted](https://github.com/twisted/twisted)) - An event-driven networking engine.
- Parallelism
  - 🌎 [concurrent.futures](docs.python.org/3/library/concurrent.futures.html) - (Python standard library) A high-level interface for asynchronously executing callables.
  - 🌎 [multiprocessing](docs.python.org/3/library/multiprocessing.html) - (Python standard library) Process-based parallelism.

### Date and Time

_Libraries for working with dates and times._

- 🌎 [zoneinfo](docs.python.org/3/library/zoneinfo.html) - (Python standard library) IANA time zone support. Brings the 🌎 [tz database](en.wikipedia.org/wiki/Tz_database) into Python.
- <b><code>&nbsp;&nbsp;2634⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;578🍴</code></b> [python-dateutil](https://github.com/dateutil/dateutil)) - Extensions to the standard Python 🌎 [datetime](docs.python.org/3/library/datetime.html) module.
- <b><code>&nbsp;&nbsp;2859⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;518🍴</code></b> [dateparser](https://github.com/scrapinghub/dateparser)) - A Python parser for human-readable dates in dozens of languages.
- <b><code>&nbsp;&nbsp;6674⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;453🍴</code></b> [pendulum](https://github.com/python-pendulum/pendulum)) - Python datetimes made easy.
- <b><code>&nbsp;&nbsp;2404⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;38🍴</code></b> [whenever](https://github.com/ariebovenberg/whenever)) - A modern datetime library, type-safe and DST-safe, backed by Rust.

**Python Toolchain**

### Environment Management

_Libraries for Python version and virtual environment management._

- <b><code>&nbsp;&nbsp;5048⭐</code></b> <b><code>&nbsp;&nbsp;1116🍴</code></b> [virtualenv](https://github.com/pypa/virtualenv)) - A tool to create isolated Python environments.
- <b><code>&nbsp;89941⭐</code></b> <b><code>&nbsp;&nbsp;3590🍴</code></b> [uv](https://github.com/astral-sh/uv)) - An extremely fast Python version, package and project manager, written in Rust.
- <b><code>&nbsp;45103⭐</code></b> <b><code>&nbsp;&nbsp;3274🍴</code></b> [pyenv](https://github.com/pyenv/pyenv)) - Simple Python version management.

### Package Management

_Libraries for package and dependency management._

- Package Managers
  - <b><code>&nbsp;10288⭐</code></b> <b><code>&nbsp;&nbsp;3377🍴</code></b> [pip](https://github.com/pypa/pip)) - The package installer for Python.
  - <b><code>&nbsp;89941⭐</code></b> <b><code>&nbsp;&nbsp;3590🍴</code></b> [uv](https://github.com/astral-sh/uv)) - An extremely fast Python version, package and project manager, written in Rust.
  - <b><code>&nbsp;34303⭐</code></b> <b><code>&nbsp;&nbsp;2494🍴</code></b> [poetry](https://github.com/python-poetry/poetry)) - Python dependency management and packaging made easy.
  - <b><code>&nbsp;&nbsp;7235⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;459🍴</code></b> [hatch](https://github.com/pypa/hatch)) - Modern, extensible Python project manager for environments, builds, and publishing.
  - <b><code>&nbsp;12967⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;596🍴</code></b> [pipx](https://github.com/pypa/pipx)) - Install and Run Python Applications in Isolated Environments. Like `npx` in Node.js.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [conda](https://github.com/conda/conda/)) - Cross-platform, Python-agnostic binary package manager.
- Build Backends
  - <b><code>&nbsp;&nbsp;2861⭐</code></b> <b><code>&nbsp;&nbsp;1429🍴</code></b> [setuptools](https://github.com/pypa/setuptools)) - The historical and still most widely used pyproject build backend.
  - <b><code>&nbsp;&nbsp;7235⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;459🍴</code></b> [hatchling](https://github.com/pypa/hatch)) - Modern, extensible build backend from the hatch project.
  - <b><code>&nbsp;89941⭐</code></b> <b><code>&nbsp;&nbsp;3590🍴</code></b> [uv-build](https://github.com/astral-sh/uv)) - uv's fast, minimal build backend for pure-Python projects.

### Package Repositories

_Local PyPI repository server and proxies._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [bandersnatch](https://github.com/pypa/bandersnatch/)) - PyPI mirroring tool provided by Python Packaging Authority (PyPA).
- <b><code>&nbsp;&nbsp;1222⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [devpi](https://github.com/devpi/devpi)) - PyPI server and packaging/testing/release tool.
- <b><code>&nbsp;&nbsp;4157⭐</code></b> <b><code>&nbsp;&nbsp;1249🍴</code></b> [warehouse](https://github.com/pypi/warehouse)) - Next generation Python Package Repository (PyPI).

### Distribution

_Libraries to create packaged executables for release distribution._

- Executables
  - <b><code>&nbsp;13095⭐</code></b> <b><code>&nbsp;&nbsp;2031🍴</code></b> [pyinstaller](https://github.com/pyinstaller/pyinstaller)) - Converts Python programs into stand-alone executables (cross-platform).
  - <b><code>&nbsp;15129⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;790🍴</code></b> [Nuitka](https://github.com/Nuitka/Nuitka)) - Compiles Python programs into high-performance standalone executables (cross-platform, supports all Python versions).
  - <b><code>&nbsp;&nbsp;1945⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;114🍴</code></b> [shiv](https://github.com/linkedin/shiv)) - A command line utility for building fully self-contained zipapps (PEP 441), but with all their dependencies included.
  - <b><code>&nbsp;&nbsp;1561⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;241🍴</code></b> [cx-Freeze](https://github.com/marcelotduarte/cx_Freeze)) - It is a Python tool that converts Python scripts into standalone executables and installers for Windows, macOS, and Linux.
- Obfuscation
  - <b><code>&nbsp;&nbsp;5189⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;364🍴</code></b> [pyarmor](https://github.com/dashingsoft/pyarmor)) - A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

### Configuration Files

_Libraries for storing and parsing configuration options._

- 🌎 [configparser](docs.python.org/3/library/configparser.html) - (Python standard library) INI file parser.
- <b><code>&nbsp;&nbsp;8877⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;580🍴</code></b> [python-dotenv](https://github.com/theskumar/python-dotenv)) - Reads key-value pairs from a `.env` file and sets them as environment variables.
- <b><code>&nbsp;&nbsp;1457⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;195🍴</code></b> [pydantic-settings](https://github.com/pydantic/pydantic-settings)) - Settings management using Pydantic models with validation, loading from environment variables and secrets files.
- <b><code>&nbsp;10659⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;980🍴</code></b> [hydra-core](https://github.com/facebookresearch/hydra)) - Hydra is a framework for elegantly configuring complex applications.
- <b><code>&nbsp;&nbsp;4331⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;346🍴</code></b> [dynaconf](https://github.com/dynaconf/dynaconf)) - Dynaconf is a configuration manager with plugins for Django, Flask and FastAPI.

**Security**

### Cryptography

_Libraries for cryptographic primitives and secure protocols._

- <b><code>&nbsp;&nbsp;7771⭐</code></b> <b><code>&nbsp;&nbsp;1824🍴</code></b> [cryptography](https://github.com/pyca/cryptography)) - A package designed to expose cryptographic primitives and recipes to Python developers.
- <b><code>&nbsp;&nbsp;1206⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;266🍴</code></b> [pynacl](https://github.com/pyca/pynacl)) - Python binding to the Networking and Cryptography (NaCl) library.
- <b><code>&nbsp;&nbsp;9853⭐</code></b> <b><code>&nbsp;&nbsp;2075🍴</code></b> [paramiko](https://github.com/paramiko/paramiko)) - The leading native Python SSHv2 protocol library.
- <b><code>&nbsp;&nbsp;3134⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;279🍴</code></b> [itsdangerous](https://github.com/pallets/itsdangerous)) - Various helpers to pass trusted data to untrusted environments.

### Penetration Testing

_Frameworks and tools for penetration testing._

- <b><code>&nbsp;45080⭐</code></b> <b><code>&nbsp;&nbsp;4730🍴</code></b> [mitmproxy](https://github.com/mitmproxy/mitmproxy)) - An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.
- <b><code>&nbsp;38463⭐</code></b> <b><code>&nbsp;&nbsp;6365🍴</code></b> [sqlmap](https://github.com/sqlmapproject/sqlmap)) - Automatic SQL injection and database takeover tool.
- <b><code>&nbsp;92003⭐</code></b> <b><code>&nbsp;10841🍴</code></b> [sherlock-project](https://github.com/sherlock-project/sherlock)) - Hunt down social media accounts by username across social networks.
- <b><code>&nbsp;15307⭐</code></b> <b><code>&nbsp;&nbsp;3408🍴</code></b> [social-engineer-toolkit](https://github.com/trustedsec/social-engineer-toolkit)) - A toolkit for social engineering.

### Supply Chain Security

_Tools for auditing dependencies against known vulnerabilities._

- <b><code>&nbsp;&nbsp;1364⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;132🍴</code></b> [pip-audit](https://github.com/pypa/pip-audit)) - Audits Python environments and dependency trees for known vulnerabilities, using the PyPI Advisory Database and OSV.
- <b><code>&nbsp;89941⭐</code></b> <b><code>&nbsp;&nbsp;3590🍴</code></b> [uv-audit](https://github.com/astral-sh/uv)) - (part of uv) uv's 🌎 [dependency vulnerability and malware scanning](docs.astral.sh/uv/reference/cli/#uv-audit) backed by OSV.

### Web Security

_Libraries for application-layer web security._

- <b><code>&nbsp;&nbsp;1055⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33🍴</code></b> [secure](https://github.com/TypeError/secure)) - HTTP security headers for Python web applications with ASGI and WSGI middleware.

**Other**

### Hardware

_Libraries for programming with hardware._

- <b><code>&nbsp;&nbsp;2521⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;368🍴</code></b> [bleak](https://github.com/hbldh/bleak)) - A cross platform Bluetooth Low Energy Client for Python using asyncio.
- <b><code>&nbsp;&nbsp;2170⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;285🍴</code></b> [pynput](https://github.com/moses-palmer/pynput)) - A library to control and monitor input devices.
- <b><code>&nbsp;&nbsp;&nbsp;219⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;37🍴</code></b> [jumpstarter](https://github.com/jumpstarter-dev/jumpstarter)) - A hardware-in-the-loop testing framework with a Python client library for automated testing on real and virtual hardware.

### Microsoft Windows

_Python programming on Microsoft Windows._

- <b><code>&nbsp;&nbsp;5513⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;780🍴</code></b> [pythonnet](https://github.com/pythonnet/pythonnet)) - Python Integration with the .NET Common Language Runtime (CLR).
- <b><code>&nbsp;&nbsp;5603⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;849🍴</code></b> [pywin32](https://github.com/mhammond/pywin32)) - Python Extensions for Windows.
- <b><code>&nbsp;&nbsp;7399⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;594🍴</code></b> [pyenv-win](https://github.com/pyenv-win/pyenv-win)) - A Python version manager for Windows (<b><code>&nbsp;45103⭐</code></b> <b><code>&nbsp;&nbsp;3274🍴</code></b> [pyenv](https://github.com/pyenv/pyenv)) fork).
- <b><code>&nbsp;&nbsp;2280⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;350🍴</code></b> [winpython](https://github.com/winpython/winpython)) - Portable development environment for Windows 10/11.

### Miscellaneous

_Useful libraries or tools that don't fit in the categories above._

- <b><code>&nbsp;&nbsp;2093⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;191🍴</code></b> [blinker](https://github.com/pallets-eco/blinker)) - A fast Python in-process signal/event dispatching system.
- <b><code>&nbsp;&nbsp;6924⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;440🍴</code></b> [boltons](https://github.com/mahmoud/boltons)) - A set of pure-Python utilities.

## Resources

Where to discover learning resources or new Python libraries.

### Newsletters

- 🌎 [Awesome Python Newsletter](python.libhunt.com/newsletter)
- 🌎 [Pycoder's Weekly](pycoders.com/)
- 🌎 [Python Tricks](realpython.com/python-tricks/)
- 🌎 [Python Weekly](www.pythonweekly.com/)

### Podcasts

- 🌎 [Django Chat](djangochat.com/)
- 🌎 [PyPodcats](pypodcats.live)
- 🌎 [Python Bytes](pythonbytes.fm)
- 🌎 [Talk Python To Me](talkpython.fm/)
- 🌎 [The Real Python Podcast](realpython.com/podcasts/rpp/)

### Websites

- 🌎 [Python Developer Tooling Handbook](pydevtools.com/) - Comprehensive guide to modern Python developer tools covering package management, linting, type checking, testing, and more.

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](https://github.com/correia-jpv/fucking-awesome-python/blob/master/CONTRIBUTING.md) first.

---

If you have any question about this opinionated list, do not hesitate to contact 🌎 [@vinta](x.com/vinta) on X (Twitter).

## Source
<b><code>321362⭐</code></b> <b><code>&nbsp;28755🍴</code></b> [vinta/awesome-python](https://github.com/vinta/awesome-python))