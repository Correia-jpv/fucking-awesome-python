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
  - <b><code>&nbsp;&nbsp;&nbsp;149⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [django-ai-plugins](https://github.com/vintasoftware/django-ai-plugins)) - Django backend agent skills for Django, DRF, Celery, and Django-specific code review.
  - <b><code>&nbsp;&nbsp;1032⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;53🍴</code></b> [sentry-skills](https://github.com/getsentry/skills)) - Agent skills the Sentry team uses for code review, pull requests, and Django reviews.
  - <b><code>&nbsp;&nbsp;7338⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;625🍴</code></b> [trailofbits-skills](https://github.com/trailofbits/skills)) - Security skills for vulnerability detection, auditing, and testing.
- Orchestration
  - <b><code>147378⭐</code></b> <b><code>&nbsp;24684🍴</code></b> [langchain](https://github.com/langchain-ai/langchain)) - A framework for building agents and LLM-powered applications.
  - <b><code>&nbsp;42601⭐</code></b> <b><code>&nbsp;&nbsp;7223🍴</code></b> [langgraph](https://github.com/langchain-ai/langgraph)) - Low-level orchestration framework for building stateful, long-running LLM agents.
  - <b><code>&nbsp;20350⭐</code></b> <b><code>&nbsp;&nbsp;2844🍴</code></b> [pydantic-ai](https://github.com/pydantic/pydantic-ai)) - A Python agent framework for building generative AI applications with structured schemas.
  - <b><code>&nbsp;59283⭐</code></b> <b><code>&nbsp;&nbsp;8624🍴</code></b> [crewai](https://github.com/crewAIInc/crewAI)) - A framework for orchestrating role-playing autonomous AI agents for collaborative task solving.
- Vendor Agent SDKs
  - <b><code>&nbsp;&nbsp;8201⭐</code></b> <b><code>&nbsp;&nbsp;1314🍴</code></b> [claude-agent-sdk](https://github.com/anthropics/claude-agent-sdk-python)) - Anthropic's Python SDK for building AI agents on Claude Code's harness — custom tools, in-process MCP servers, hooks.
  - <b><code>&nbsp;29799⭐</code></b> <b><code>&nbsp;&nbsp;4843🍴</code></b> [openai-agents](https://github.com/openai/openai-agents-python)) - OpenAI's framework for building and managing AI agents.
  - <b><code>&nbsp;21690⭐</code></b> <b><code>&nbsp;&nbsp;4088🍴</code></b> [google-adk](https://github.com/google/adk-python)) - Google's code-first toolkit for building, evaluating, and deploying AI agents.
- Model Context Protocol
  - <b><code>&nbsp;24452⭐</code></b> <b><code>&nbsp;&nbsp;4000🍴</code></b> [mcp](https://github.com/modelcontextprotocol/python-sdk)) - The official Python SDK for building Model Context Protocol servers and clients.
  - <b><code>&nbsp;27957⭐</code></b> <b><code>&nbsp;&nbsp;2423🍴</code></b> [fastmcp](https://github.com/PrefectHQ/fastmcp)) - A high-level, Pythonic framework for building MCP servers and clients.
- Personal Assistants
  - <b><code>250676⭐</code></b> <b><code>&nbsp;53691🍴</code></b> [hermes-agent](https://github.com/NousResearch/hermes-agent)) - An adaptive personal AI assistant that grows with you.
  - <b><code>&nbsp;41294⭐</code></b> <b><code>&nbsp;&nbsp;3006🍴</code></b> [AstrBot](https://github.com/AstrBotDevs/AstrBot)) - A multi-platform AI assistant that connects LLMs to chat apps like Telegram, Slack, and QQ, extensible with Python plugins.
- Prompt Optimization
  - <b><code>&nbsp;38465⭐</code></b> <b><code>&nbsp;&nbsp;3388🍴</code></b> [dspy](https://github.com/stanfordnlp/dspy)) - A framework for programming, not prompting, language models.
- Data Layer
  - <b><code>&nbsp;13970⭐</code></b> <b><code>&nbsp;&nbsp;1282🍴</code></b> [instructor](https://github.com/567-labs/instructor)) - A library for extracting structured data from LLMs, powered by Pydantic.
  - <b><code>&nbsp;52383⭐</code></b> <b><code>&nbsp;&nbsp;8263🍴</code></b> [llama-index](https://github.com/run-llama/llama_index)) - A toolkit for building RAG pipelines and agents over your data.
  - <b><code>&nbsp;66459⭐</code></b> <b><code>&nbsp;&nbsp;7831🍴</code></b> [mem0](https://github.com/mem0ai/mem0)) - An intelligent memory layer for AI agents enabling personalized interactions.
  - <b><code>&nbsp;39127⭐</code></b> <b><code>&nbsp;&nbsp;3071🍴</code></b> [openviking](https://github.com/volcengine/OpenViking)) - A context database for AI agents that unifies memory, resources, and skills.
  - <b><code>&nbsp;13612⭐</code></b> <b><code>&nbsp;&nbsp;1559🍴</code></b> [semantica](https://github.com/semantica-agi/semantica)) - A graph-native context and knowledge layer for AI agents with reasoning, provenance, and governance.
- Pre-trained Models
  - <b><code>166906⭐</code></b> <b><code>&nbsp;34742🍴</code></b> [transformers](https://github.com/huggingface/transformers)) - The model-definition framework for pretrained models in text, computer vision, audio, video, and multimodal tasks, for inference and training.
- LLM Inference and Serving
  - <b><code>&nbsp;36716⭐</code></b> <b><code>&nbsp;&nbsp;9264🍴</code></b> [sglang](https://github.com/sgl-project/sglang)) - A high-performance serving framework for large language models and multimodal models.
  - <b><code>&nbsp;93060⭐</code></b> <b><code>&nbsp;22928🍴</code></b> [vllm](https://github.com/vllm-project/vllm)) - A high-throughput and memory-efficient inference and serving engine for LLMs.
  - <b><code>&nbsp;&nbsp;7198⭐</code></b> <b><code>&nbsp;&nbsp;1092🍴</code></b> [mlx-lm](https://github.com/ml-explore/mlx-lm)) - Run and fine-tune large language models on Apple Silicon with MLX.
- LLM Gateways
  - <b><code>&nbsp;60032⭐</code></b> <b><code>&nbsp;11965🍴</code></b> [litellm](https://github.com/BerriAI/litellm)) - Call 100+ LLMs using OpenAI format.
- Image and Video Generation
  - <b><code>&nbsp;34641⭐</code></b> <b><code>&nbsp;&nbsp;7368🍴</code></b> [diffusers](https://github.com/huggingface/diffusers)) - A library that provides pre-trained diffusion models for generating and editing images, audio, and video.
- Fine-tuning
  - <b><code>&nbsp;21748⭐</code></b> <b><code>&nbsp;&nbsp;2543🍴</code></b> [peft](https://github.com/huggingface/peft)) - A library for parameter-efficient fine-tuning of large pretrained models.
  - <b><code>&nbsp;19436⭐</code></b> <b><code>&nbsp;&nbsp;3036🍴</code></b> [trl](https://github.com/huggingface/trl)) - A library for post-training transformer language models with SFT, DPO, GRPO, and other trainers.
  - <b><code>&nbsp;77135⭐</code></b> <b><code>&nbsp;&nbsp;7096🍴</code></b> [unsloth](https://github.com/unslothai/unsloth)) - Faster, lower-memory LLM fine-tuning, as a Python library or a desktop app.
  - <b><code>&nbsp;12513⭐</code></b> <b><code>&nbsp;&nbsp;1452🍴</code></b> [axolotl](https://github.com/axolotl-ai-cloud/axolotl)) - A framework for fine-tuning and post-training large language models.
- Speech
  - <b><code>&nbsp;25672⭐</code></b> <b><code>&nbsp;&nbsp;2107🍴</code></b> [faster-whisper](https://github.com/SYSTRAN/faster-whisper)) - A Whisper reimplementation on CTranslate2, up to 4 times faster than openai-whisper with less memory.
  - <b><code>109870⭐</code></b> <b><code>&nbsp;13319🍴</code></b> [openai-whisper](https://github.com/openai/whisper)) - A general-purpose automatic speech recognition model trained on 680k hours of multilingual and multitask supervised data.
  - <b><code>&nbsp;&nbsp;2633⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;390🍴</code></b> [gTTS](https://github.com/pndurette/gTTS)) - Python library and CLI tool for converting text to speech using Google Translate TTS.
  - <b><code>&nbsp;20570⭐</code></b> <b><code>&nbsp;&nbsp;2054🍴</code></b> [funasr](https://github.com/modelscope/FunASR)) - Industrial-grade speech recognition toolkit with speaker diarization and emotion detection.

### Deep Learning

_Frameworks for Neural Networks and Deep Learning. Also see <b><code>&nbsp;28999⭐</code></b> <b><code>&nbsp;&nbsp;6350🍴</code></b> [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning))._

- Frameworks
  - <b><code>103611⭐</code></b> <b><code>&nbsp;31054🍴</code></b> [pytorch](https://github.com/pytorch/pytorch)) - Tensors and Dynamic neural networks in Python with strong GPU acceleration.
  - <b><code>&nbsp;31372⭐</code></b> <b><code>&nbsp;&nbsp;3805🍴</code></b> [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)) - Deep learning framework to train, deploy, and ship AI products Lightning fast.
  - <b><code>&nbsp;36370⭐</code></b> <b><code>&nbsp;&nbsp;3830🍴</code></b> [jax](https://github.com/jax-ml/jax)) - A library for high-performance numerical computing with automatic differentiation and JIT compilation.
  - <b><code>&nbsp;64346⭐</code></b> <b><code>&nbsp;19805🍴</code></b> [keras](https://github.com/keras-team/keras)) - A high-level deep learning library with support for JAX, TensorFlow, and PyTorch backends.
  - <b><code>200665⭐</code></b> <b><code>&nbsp;78006🍴</code></b> [tensorflow](https://github.com/tensorflow/tensorflow)) - An end-to-end machine learning platform from Google.
- Reinforcement Learning
  - <b><code>&nbsp;12609⭐</code></b> <b><code>&nbsp;&nbsp;1489🍴</code></b> [gymnasium](https://github.com/Farama-Foundation/Gymnasium)) - A standard API for reinforcement learning environments with popular reference environments (<b><code>&nbsp;37238⭐</code></b> <b><code>&nbsp;&nbsp;8671🍴</code></b> [gym](https://github.com/openai/gym)) successor).
  - <b><code>&nbsp;13862⭐</code></b> <b><code>&nbsp;&nbsp;2183🍴</code></b> [stable-baselines3](https://github.com/DLR-RM/stable-baselines3)) - PyTorch implementations of Stable Baselines (deep) reinforcement learning algorithms.

### Machine Learning

_Libraries for Machine Learning. Also see <b><code>&nbsp;74506⭐</code></b> <b><code>&nbsp;15661🍴</code></b> [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python))._

- General
  - <b><code>&nbsp;67449⭐</code></b> <b><code>&nbsp;27470🍴</code></b> [scikit-learn](https://github.com/scikit-learn/scikit-learn)) - The most popular Python library for Machine Learning with extensive documentation and community support.
  - <b><code>&nbsp;&nbsp;3345⭐</code></b> <b><code>&nbsp;&nbsp;1176🍴</code></b> [pgmpy](https://github.com/pgmpy/pgmpy)) - A Python library for causal and probabilistic reasoning with graphical models.
  - <b><code>&nbsp;&nbsp;2284⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;379🍴</code></b> [feature-engine](https://github.com/feature-engine/feature_engine)) - sklearn compatible API with the widest toolset for feature engineering and selection.
- Gradient Boosting
  - <b><code>&nbsp;28811⭐</code></b> <b><code>&nbsp;&nbsp;8924🍴</code></b> [xgboost](https://github.com/dmlc/xgboost)) - A scalable, portable, and distributed gradient boosting library.
  - <b><code>&nbsp;18826⭐</code></b> <b><code>&nbsp;&nbsp;4081🍴</code></b> [lightgbm](https://github.com/lightgbm-org/LightGBM)) - A fast, distributed, high performance gradient boosting framework.
  - <b><code>&nbsp;&nbsp;9130⭐</code></b> <b><code>&nbsp;&nbsp;1341🍴</code></b> [catboost](https://github.com/catboost/catboost)) - A fast, scalable, high performance gradient boosting on decision trees library.
- Time Series Forecasting
  - <b><code>&nbsp;20428⭐</code></b> <b><code>&nbsp;&nbsp;4637🍴</code></b> [prophet](https://github.com/facebook/prophet)) - A tool for producing forecasts for time series with multiple seasonality and trend changes.
  - <b><code>&nbsp;&nbsp;4919⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;400🍴</code></b> [statsforecast](https://github.com/Nixtla/statsforecast)) - Fast statistical forecasting models such as ARIMA, ETS, and Theta, compiled with numba.
  - <b><code>&nbsp;10049⭐</code></b> <b><code>&nbsp;&nbsp;2409🍴</code></b> [sktime](https://github.com/sktime/sktime)) - A unified scikit-learn-style framework for forecasting and other time-series learning tasks.
  - <b><code>&nbsp;34054⭐</code></b> <b><code>&nbsp;&nbsp;3287🍴</code></b> [timesfm](https://github.com/google-research/timesfm)) - A pretrained foundation model from Google Research for time-series forecasting, with non-commercial default weights.

### Natural Language Processing

_Libraries for working with human languages._

- General
  - <b><code>&nbsp;14733⭐</code></b> <b><code>&nbsp;&nbsp;3045🍴</code></b> [nltk](https://github.com/nltk/nltk)) - A leading platform for building Python programs to work with human language data.
  - <b><code>&nbsp;33934⭐</code></b> <b><code>&nbsp;&nbsp;4733🍴</code></b> [spacy](https://github.com/explosion/spaCy)) - A library for industrial-strength natural language processing in Python and Cython.
  - <b><code>&nbsp;16494⭐</code></b> <b><code>&nbsp;&nbsp;4401🍴</code></b> [gensim](https://github.com/piskvorky/gensim)) - Topic Modeling for Humans.
  - <b><code>&nbsp;&nbsp;7890⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;961🍴</code></b> [stanza](https://github.com/stanfordnlp/stanza)) - The Stanford NLP Group's official Python library, supporting 60+ languages.
- Chinese
  - <b><code>&nbsp;35174⭐</code></b> <b><code>&nbsp;&nbsp;6677🍴</code></b> [jieba](https://github.com/fxsjy/jieba)) - The most popular Chinese text segmentation library.
  - <b><code>&nbsp;&nbsp;5367⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;629🍴</code></b> [pypinyin](https://github.com/mozillazg/python-pinyin)) - Convert Chinese hanzi (漢字) to pinyin (拼音).
  - <b><code>&nbsp;&nbsp;&nbsp;280⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [pangu.py](https://github.com/vinta/pangu.py)) - Paranoid text spacing.

### Computer Vision

_Libraries for image and video analysis, object detection, and OCR._

- General
  - <b><code>&nbsp;&nbsp;5413⭐</code></b> <b><code>&nbsp;&nbsp;1045🍴</code></b> [opencv-python](https://github.com/opencv/opencv-python)) - Open Source Computer Vision Library.
  - <b><code>&nbsp;62156⭐</code></b> <b><code>&nbsp;11814🍴</code></b> [ultralytics](https://github.com/ultralytics/ultralytics)) - Ultralytics YOLO for object detection, segmentation, pose estimation, classification, and tracking.
  - <b><code>&nbsp;11391⭐</code></b> <b><code>&nbsp;&nbsp;1351🍴</code></b> [kornia](https://github.com/kornia/kornia)) - Open Source Differentiable Computer Vision Library for PyTorch.
  - <b><code>&nbsp;11137⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;833🍴</code></b> [fiftyone](https://github.com/voxel51/fiftyone)) - The open-source tool for building high-quality datasets and computer vision models.
- OCR
  - <b><code>&nbsp;&nbsp;6393⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;748🍴</code></b> [pytesseract](https://github.com/madmaze/pytesseract)) - A wrapper for the <b><code>&nbsp;76796⭐</code></b> <b><code>&nbsp;10819🍴</code></b> [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)) engine.
  - <b><code>&nbsp;30044⭐</code></b> <b><code>&nbsp;&nbsp;3611🍴</code></b> [easyocr](https://github.com/JaidedAI/EasyOCR)) - Ready-to-use OCR with 80+ languages supported.
  - <b><code>&nbsp;90509⭐</code></b> <b><code>&nbsp;11434🍴</code></b> [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)) - Multilingual OCR and document parsing toolkit based on PaddlePaddle.

### Recommender Systems

_Libraries for building recommender systems._

- <b><code>&nbsp;14310⭐</code></b> <b><code>&nbsp;&nbsp;1225🍴</code></b> [annoy](https://github.com/spotify/annoy)) - Approximate Nearest Neighbors in C++/Python optimized for memory usage.
- <b><code>&nbsp;&nbsp;3826⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;632🍴</code></b> [implicit](https://github.com/benfred/implicit)) - A fast Python implementation of collaborative filtering for implicit datasets.
- <b><code>&nbsp;&nbsp;6819⭐</code></b> <b><code>&nbsp;&nbsp;1048🍴</code></b> [scikit-surprise](https://github.com/NicolasHug/Surprise)) - A scikit for building and analyzing recommender systems.

**Web Development**

### Web Frameworks

_Traditional full stack web frameworks. Also see [Web APIs](#web-apis)._

- Synchronous
  - <b><code>&nbsp;74808⭐</code></b> <b><code>&nbsp;17032🍴</code></b> [flask](https://github.com/pallets/flask)) - A microframework for Python.
    - <b><code>&nbsp;12783⭐</code></b> <b><code>&nbsp;&nbsp;1566🍴</code></b> [awesome-flask](https://github.com/humiaozuzu/awesome-flask))
  - <b><code>&nbsp;91241⭐</code></b> <b><code>&nbsp;35936🍴</code></b> [django](https://github.com/django/django)) - A high-level web framework that encourages rapid development and clean, pragmatic design.
    - <b><code>&nbsp;11266⭐</code></b> <b><code>&nbsp;&nbsp;1473🍴</code></b> [awesome-django](https://github.com/wsvincent/awesome-django))
  - <b><code>&nbsp;&nbsp;8792⭐</code></b> <b><code>&nbsp;&nbsp;1512🍴</code></b> [bottle](https://github.com/bottlepy/bottle)) - A fast and simple micro-framework distributed as a single file with no dependencies.
  - <b><code>&nbsp;&nbsp;4100⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;893🍴</code></b> [pyramid](https://github.com/Pylons/pyramid)) - A small, fast, down-to-earth, open source Python web framework.
  - <b><code>&nbsp;&nbsp;7047⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;325🍴</code></b> [fasthtml](https://github.com/AnswerDotAI/fasthtml)) - The fastest way to create an HTML app.
- Asynchronous
  - <b><code>&nbsp;12644⭐</code></b> <b><code>&nbsp;&nbsp;1352🍴</code></b> [starlette](https://github.com/Kludex/starlette)) - A lightweight ASGI framework and toolkit for building high-performance async services.
  - <b><code>&nbsp;22171⭐</code></b> <b><code>&nbsp;&nbsp;5562🍴</code></b> [tornado](https://github.com/tornadoweb/tornado)) - A web framework and asynchronous networking library.
  - <b><code>&nbsp;&nbsp;8488⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;657🍴</code></b> [litestar](https://github.com/litestar-org/litestar)) - Production-ready, capable and extensible ASGI Web framework.
  - <b><code>&nbsp;28928⭐</code></b> <b><code>&nbsp;&nbsp;1790🍴</code></b> [reflex](https://github.com/reflex-dev/reflex)) - A framework for building reactive, full-stack web applications entirely with Python.

### Web APIs

_Libraries for building RESTful, GraphQL, and RPC APIs._

- Django
  - <b><code>&nbsp;30199⭐</code></b> <b><code>&nbsp;&nbsp;7086🍴</code></b> [django-rest-framework](https://github.com/encode/django-rest-framework)) - A powerful and flexible toolkit to build web APIs.
  - <b><code>&nbsp;&nbsp;9204⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;614🍴</code></b> [django-ninja](https://github.com/vitalik/django-ninja)) - Fast, Django REST framework based on type hints and Pydantic.
  - <b><code>&nbsp;&nbsp;&nbsp;504⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;155🍴</code></b> [strawberry-django](https://github.com/strawberry-graphql/strawberry-django)) - Strawberry GraphQL integration with Django.
  - <b><code>&nbsp;&nbsp;1491⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;221🍴</code></b> [django-modern-rest](https://github.com/wemake-services/django-modern-rest)) - Modern REST with speed, types, async, `msgspec`, `pydantic` and other goodies!
- Flask
  - <b><code>&nbsp;&nbsp;2232⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;347🍴</code></b> [flask-restx](https://github.com/python-restx/flask-restx)) - Fully featured framework for fast, easy and documented API development with Flask.
  - <b><code>&nbsp;&nbsp;&nbsp;717⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;77🍴</code></b> [flask-smorest](https://github.com/marshmallow-code/flask-smorest)) - A Flask/Marshmallow-based REST API framework with automatic OpenAPI documentation.
  - <b><code>&nbsp;&nbsp;1138⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;145🍴</code></b> [apiflask](https://github.com/apiflask/apiflask)) - A lightweight Python web API framework based on Flask, supporting marshmallow schemas and Pydantic models.
- Framework Agnostic
  - <b><code>102759⭐</code></b> <b><code>&nbsp;&nbsp;9981🍴</code></b> [fastapi](https://github.com/fastapi/fastapi)) - A modern, fast, web framework for building APIs with standard Python type hints.
  - <b><code>&nbsp;&nbsp;4722⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;664🍴</code></b> [strawberry](https://github.com/strawberry-graphql/strawberry)) - A GraphQL library that leverages Python type annotations for schema definition.
  - <b><code>&nbsp;&nbsp;4614⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;787🍴</code></b> [connexion](https://github.com/spec-first/connexion)) - A spec-first framework that automatically handles requests based on your OpenAPI specification.
- RPC
  - <b><code>&nbsp;45359⭐</code></b> <b><code>&nbsp;11377🍴</code></b> [grpcio](https://github.com/grpc/grpc)) - HTTP/2-based RPC framework with Python bindings, built by Google.

### Web Servers

_ASGI and WSGI compatible web servers._

- ASGI
  - <b><code>&nbsp;11002⭐</code></b> <b><code>&nbsp;&nbsp;1055🍴</code></b> [uvicorn](https://github.com/Kludex/uvicorn)) - A lightning-fast ASGI server implementation.
  - <b><code>&nbsp;&nbsp;5681⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;177🍴</code></b> [granian](https://github.com/emmett-framework/granian)) - A Rust HTTP server for Python applications built on top of Hyper and Tokio, supporting WSGI/ASGI/RSGI.
  - <b><code>&nbsp;&nbsp;1615⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;172🍴</code></b> [hypercorn](https://github.com/pgjones/hypercorn)) - An ASGI and WSGI Server based on Hyper libraries and inspired by Gunicorn.
- WSGI
  - <b><code>&nbsp;10692⭐</code></b> <b><code>&nbsp;&nbsp;1863🍴</code></b> [gunicorn](https://github.com/benoitc/gunicorn)) - A pre-fork WSGI server with a native ASGI worker, ported from Ruby's Unicorn project.
  - <b><code>&nbsp;&nbsp;1601⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;190🍴</code></b> [waitress](https://github.com/Pylons/waitress)) - Multi-threaded, powers Pyramid.

### WebSocket

_Libraries for working with WebSocket._

- <b><code>&nbsp;&nbsp;5723⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;617🍴</code></b> [websockets](https://github.com/python-websockets/websockets)) - A library for building WebSocket servers and clients with a focus on correctness and simplicity.
- <b><code>&nbsp;&nbsp;6360⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;826🍴</code></b> [channels](https://github.com/django/channels)) - Brings WebSocket, long-poll HTTP, and other async support to Django.
- <b><code>&nbsp;&nbsp;5507⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;904🍴</code></b> [flask-socketio](https://github.com/miguelgrinberg/Flask-SocketIO)) - Socket.IO integration for Flask applications.
- <b><code>&nbsp;&nbsp;2541⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;770🍴</code></b> [autobahn-python](https://github.com/crossbario/autobahn-python)) - WebSocket & WAMP for Python on Twisted and 🌎 [asyncio](docs.python.org/3/library/asyncio.html).

### Template Engines

_Libraries for rendering text and HTML from templates._

- <b><code>&nbsp;11795⭐</code></b> <b><code>&nbsp;&nbsp;1847🍴</code></b> [jinja](https://github.com/pallets/jinja)) - A modern and designer friendly templating language.
- <b><code>&nbsp;&nbsp;&nbsp;459⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;96🍴</code></b> [mako](https://github.com/sqlalchemy/mako)) - Hyperfast and lightweight templating for the Python platform.

### Web Asset Management

_Tools for managing, storing, compressing and minifying website assets._

- <b><code>&nbsp;&nbsp;2762⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;156🍴</code></b> [whitenoise](https://github.com/evansd/whitenoise)) - Radically simplified static file serving for WSGI applications, with compression and caching headers.
- <b><code>&nbsp;&nbsp;2961⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;896🍴</code></b> [django-storages](https://github.com/jschneier/django-storages)) - A collection of custom storage back ends for Django.
- <b><code>&nbsp;&nbsp;2869⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;603🍴</code></b> [django-compressor](https://github.com/django-compressor/django-compressor)) - Compresses linked and inline JavaScript or CSS into a single cached file.

### Authentication

_Libraries for implementing authentication schemes._

- OAuth
  - <b><code>&nbsp;&nbsp;2985⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;533🍴</code></b> [oauthlib](https://github.com/oauthlib/oauthlib)) - A generic and thorough implementation of the OAuth request-signing logic.
  - <b><code>&nbsp;&nbsp;5429⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;568🍴</code></b> [authlib](https://github.com/authlib/authlib)) - A comprehensive library for building OAuth, OpenID Connect, and JWT/JWS/JWE/JWK/JWA.
  - <b><code>&nbsp;10379⭐</code></b> <b><code>&nbsp;&nbsp;3107🍴</code></b> [django-allauth](https://github.com/pennersr/django-allauth)) - Authentication app for Django that "just works."
  - <b><code>&nbsp;&nbsp;3341⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;861🍴</code></b> [django-oauth-toolkit](https://github.com/django-oauth/django-oauth-toolkit)) - An OAuth 2.0 authorization server for Django.
- JWT
  - <b><code>&nbsp;&nbsp;5710⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;799🍴</code></b> [pyjwt](https://github.com/jpadilla/pyjwt)) - JSON Web Token implementation in Python.
- Permissions
  - <b><code>&nbsp;&nbsp;3917⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;598🍴</code></b> [django-guardian](https://github.com/django-guardian/django-guardian)) - Implementation of per-object permissions for Django.
  - <b><code>&nbsp;&nbsp;1975⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;151🍴</code></b> [django-rules](https://github.com/dfunckt/django-rules)) - A tiny but powerful app providing object-level permissions to Django, without requiring a database.

### Admin Panels

_Libraries for administrative interfaces._

- <b><code>&nbsp;&nbsp;6067⭐</code></b> <b><code>&nbsp;&nbsp;1648🍴</code></b> [flask-admin](https://github.com/pallets-eco/flask-admin)) - Simple and extensible administrative interface framework for Flask.
- <b><code>&nbsp;&nbsp;3708⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;373🍴</code></b> [django-unfold](https://github.com/unfoldadmin/django-unfold)) - A modern Django admin theme for building dashboards, internal tools, and business applications.
- <b><code>&nbsp;&nbsp;2837⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;301🍴</code></b> [sqladmin](https://github.com/smithyhq/sqladmin)) - An admin interface for SQLAlchemy models in FastAPI and Starlette.
- <b><code>&nbsp;&nbsp;3947⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;651🍴</code></b> [django-grappelli](https://github.com/sehmaschine/django-grappelli)) - A jazzy skin for the Django Admin-Interface.

### CMS

_Content Management Systems._

- <b><code>&nbsp;20514⭐</code></b> <b><code>&nbsp;&nbsp;4637🍴</code></b> [wagtail](https://github.com/wagtail/wagtail)) - A Django content management system.
- <b><code>&nbsp;10676⭐</code></b> <b><code>&nbsp;&nbsp;3192🍴</code></b> [django-cms](https://github.com/django-cms/django-cms)) - The easy-to-use and developer-friendly enterprise CMS powered by Django.

### ERP

_Enterprise resource planning frameworks._

- <b><code>&nbsp;54795⭐</code></b> <b><code>&nbsp;33911🍴</code></b> [odoo](https://github.com/odoo/odoo)) - A suite of open source business apps: CRM, e-commerce, accounting, inventory, and thousands of community modules.

### Static Site Generators

_Static site generator is a software that takes some text + templates as input and produces HTML files on the output._

- <b><code>&nbsp;13345⭐</code></b> <b><code>&nbsp;&nbsp;1822🍴</code></b> [pelican](https://github.com/getpelican/pelican)) - Static site generator that supports Markdown and reST syntax.
- <b><code>&nbsp;&nbsp;2745⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;471🍴</code></b> [nikola](https://github.com/getnikola/nikola)) - A static website and blog generator.

**HTTP & Scraping**

### HTTP Clients

_Libraries for working with HTTP._

- Clients
  - <b><code>&nbsp;54373⭐</code></b> <b><code>&nbsp;11522🍴</code></b> [requests](https://github.com/psf/requests)) - HTTP Requests for Humans.
  - <b><code>&nbsp;16565⭐</code></b> <b><code>&nbsp;&nbsp;2436🍴</code></b> [aiohttp](https://github.com/aio-libs/aiohttp)) - Asynchronous HTTP client/server framework for asyncio and Python.
  - <b><code>&nbsp;&nbsp;1510⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;85🍴</code></b> [httpx2](https://github.com/pydantic/httpx2)) - HTTP/1.1 and HTTP/2 client with sync and async APIs, maintained by Pydantic (<b><code>&nbsp;15524⭐</code></b> <b><code>&nbsp;&nbsp;2676🍴</code></b> [httpx](https://github.com/encode/httpx)) fork).
  - <b><code>&nbsp;&nbsp;4068⭐</code></b> <b><code>&nbsp;&nbsp;1620🍴</code></b> [urllib3](https://github.com/urllib3/urllib3)) - An HTTP library with thread-safe connection pooling, file post, and more.
  - <b><code>&nbsp;15524⭐</code></b> <b><code>&nbsp;&nbsp;2676🍴</code></b> [httpx](https://github.com/encode/httpx)) - A next generation HTTP client for Python.
- URL Manipulation
  - <b><code>&nbsp;&nbsp;1497⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;224🍴</code></b> [yarl](https://github.com/aio-libs/yarl)) - Yet another URL library.

### Web Scraping

_Libraries to automate web scraping and extract web content._

- Frameworks
  - <b><code>116985⭐</code></b> <b><code>&nbsp;12911🍴</code></b> [browser-use](https://github.com/browser-use/browser-use)) - Make websites accessible for AI agents with easy browser automation.
  - <b><code>&nbsp;64545⭐</code></b> <b><code>&nbsp;11988🍴</code></b> [scrapy](https://github.com/scrapy/scrapy)) - A fast high-level web crawling and scraping framework.
  - <b><code>&nbsp;84637⭐</code></b> <b><code>&nbsp;&nbsp;8757🍴</code></b> [crawl4ai](https://github.com/unclecode/crawl4ai)) - An open-source, LLM-friendly web crawler that provides lightning-fast, structured data extraction specifically designed for AI agents.
  - <b><code>&nbsp;25516⭐</code></b> <b><code>&nbsp;&nbsp;1753🍴</code></b> [stagehand](https://github.com/browserbase/stagehand)) - A fast and token-efficient browser automation SDK to extract data and perform self-healing actions on web pages.
  - <b><code>&nbsp;21757⭐</code></b> <b><code>&nbsp;&nbsp;1544🍴</code></b> [jev-ultrafast](https://github.com/browser-use/jev-ultrafast)) - A fast browser agent that picks actions from an indexed table of page elements through TypeSafe's hosted Jev API, using a small LLM only to type text.
- Content Extraction
  - <b><code>&nbsp;&nbsp;2254⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;206🍴</code></b> [markdownify](https://github.com/matthewwithanm/python-markdownify)) - Convert HTML to Markdown, with customizable tag handling.
  - <b><code>&nbsp;&nbsp;2434⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;379🍴</code></b> [feedparser](https://github.com/kurtmckee/feedparser)) - Universal feed parser.
  - <b><code>&nbsp;&nbsp;6903⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;448🍴</code></b> [trafilatura](https://github.com/adbar/trafilatura)) - A tool for gathering text and metadata from the web, with built-in content filtering.

### Email

_Libraries for sending email._

- <b><code>&nbsp;&nbsp;&nbsp;432⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;62🍴</code></b> [aiosmtplib](https://github.com/cole/aiosmtplib)) - An asyncio SMTP client.
- <b><code>&nbsp;&nbsp;1904⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;150🍴</code></b> [django-anymail](https://github.com/anymail/django-anymail)) - Django email backends and webhooks for transactional email services such as Amazon SES, Brevo, Mailgun, Postmark, and Resend.
- <b><code>&nbsp;&nbsp;2736⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;266🍴</code></b> [yagmail](https://github.com/kootenpv/yagmail)) - Yet another Gmail/SMTP client.

**Database & Storage**

### ORM

_Libraries that implement Object-Relational Mapping or data mapping techniques._

- Relational Databases
  - <b><code>&nbsp;12195⭐</code></b> <b><code>&nbsp;&nbsp;1799🍴</code></b> [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)) - The Python SQL Toolkit and Object Relational Mapper.
    - <b><code>&nbsp;&nbsp;3063⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;167🍴</code></b> [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy))
  - <b><code>&nbsp;91241⭐</code></b> <b><code>&nbsp;35936🍴</code></b> [django.db.models](https://github.com/django/django)) - (part of Django) The Django 🌎 [ORM](docs.djangoproject.com/en/stable/topics/db/models/).
  - <b><code>&nbsp;11996⭐</code></b> <b><code>&nbsp;&nbsp;1385🍴</code></b> [peewee](https://github.com/coleifer/peewee)) - A small, expressive ORM.
  - <b><code>&nbsp;18354⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;890🍴</code></b> [sqlmodel](https://github.com/fastapi/sqlmodel)) - SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.
- NoSQL Databases
  - <b><code>&nbsp;&nbsp;2647⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;432🍴</code></b> [pynamodb](https://github.com/pynamodb/PynamoDB)) - A Pythonic interface for 🌎 [Amazon DynamoDB](aws.amazon.com/dynamodb/).
  - <b><code>&nbsp;&nbsp;4350⭐</code></b> <b><code>&nbsp;&nbsp;1230🍴</code></b> [mongoengine](https://github.com/MongoEngine/mongoengine)) - A Python Object-Document-Mapper for working with MongoDB.
  - <b><code>&nbsp;&nbsp;2704⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;309🍴</code></b> [beanie](https://github.com/BeanieODM/beanie)) - An asynchronous Python object-document mapper (ODM) for MongoDB.
  - <b><code>&nbsp;&nbsp;&nbsp;228⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [django-mongodb-backend](https://github.com/mongodb/django-mongodb-backend)) - Official MongoDB database backend for Django.

### Database Drivers

_Libraries for connecting and operating databases._

- MySQL - <b><code>&nbsp;&nbsp;2614⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;413🍴</code></b> [awesome-mysql](https://github.com/shlomi-noach/awesome-mysql))
  - <b><code>&nbsp;&nbsp;7853⭐</code></b> <b><code>&nbsp;&nbsp;1445🍴</code></b> [pymysql](https://github.com/PyMySQL/PyMySQL)) - A pure-Python MySQL and MariaDB client library, based on PEP 249.
  - <b><code>&nbsp;&nbsp;2537⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;444🍴</code></b> [mysqlclient](https://github.com/PyMySQL/mysqlclient)) - MySQL and MariaDB connector (<b><code>&nbsp;&nbsp;&nbsp;664⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;307🍴</code></b> [MySQLdb1](https://github.com/farcepest/MySQLdb1)) fork).
- PostgreSQL - <b><code>&nbsp;12104⭐</code></b> <b><code>&nbsp;&nbsp;1034🍴</code></b> [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres))
  - <b><code>&nbsp;&nbsp;2504⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;282🍴</code></b> [psycopg](https://github.com/psycopg/psycopg)) - A PostgreSQL adapter for Python, the successor to psycopg2.
  - <b><code>&nbsp;&nbsp;8097⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;473🍴</code></b> [asyncpg](https://github.com/MagicStack/asyncpg)) - A fast PostgreSQL Database Client Library for Python/asyncio.
- SQLite - <b><code>&nbsp;&nbsp;&nbsp;406⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;62🍴</code></b> [awesome-sqlite](https://github.com/planetopendata/awesome-sqlite))
  - 🌎 [sqlite3](docs.python.org/3/library/sqlite3.html) - (Python standard library) SQLite interface compliant with DB-API 2.0.
  - <b><code>&nbsp;&nbsp;2177⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;186🍴</code></b> [sqlite-utils](https://github.com/simonw/sqlite-utils)) - Python CLI utility and library for manipulating SQLite databases.
- ClickHouse
  - <b><code>&nbsp;&nbsp;&nbsp;523⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;164🍴</code></b> [clickhouse-connect](https://github.com/ClickHouse/clickhouse-connect)) - The official ClickHouse client, with SQLAlchemy and Superset connectors.
  - <b><code>&nbsp;&nbsp;1305⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;243🍴</code></b> [clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver)) - Python driver with native interface for ClickHouse.
- Other Relational Databases
  - <b><code>&nbsp;&nbsp;3086⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;569🍴</code></b> [pyodbc](https://github.com/mkleehammer/pyodbc)) - An ODBC bridge for connecting to SQL Server and any other ODBC-accessible database.
  - <b><code>&nbsp;&nbsp;&nbsp;454⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [oracledb](https://github.com/oracle/python-oracledb)) - The official Python driver for Oracle Database, successor to cx_Oracle.
  - <b><code>&nbsp;&nbsp;&nbsp;476⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;61🍴</code></b> [mssql-python](https://github.com/microsoft/mssql-python)) - Official Microsoft driver for SQL Server and Azure SQL, built on ODBC for high performance.
- NoSQL Databases
  - <b><code>&nbsp;13646⭐</code></b> <b><code>&nbsp;&nbsp;2761🍴</code></b> [redis](https://github.com/redis/redis-py)) - The Python client for Redis.
  - <b><code>&nbsp;&nbsp;4358⭐</code></b> <b><code>&nbsp;&nbsp;1159🍴</code></b> [pymongo](https://github.com/mongodb/mongo-python-driver)) - The official Python client for MongoDB.
  - <b><code>&nbsp;&nbsp;1429⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;587🍴</code></b> [cassandra-driver](https://github.com/apache/cassandra-python-driver)) - The Python Driver for Apache Cassandra.

### Database

_In-process databases usable directly from Python._

- Analytical
  - <b><code>&nbsp;41868⭐</code></b> <b><code>&nbsp;&nbsp;3850🍴</code></b> [duckdb](https://github.com/duckdb/duckdb)) - An in-process SQL OLAP database management system; optimized for analytics and fast queries, similar to SQLite but for analytical workloads.
  - <b><code>&nbsp;&nbsp;2910⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;136🍴</code></b> [chdb](https://github.com/chdb-io/chdb)) - In-process OLAP SQL engine with the full ClickHouse dialect, zero-copy pandas/Arrow interop, and federation to remote ClickHouse clusters via `remoteSecure()`.
- Vector
  - <b><code>&nbsp;11584⭐</code></b> <b><code>&nbsp;&nbsp;1082🍴</code></b> [lancedb](https://github.com/lancedb/lancedb)) - A developer-friendly embedded retrieval database for multimodal AI.
  - <b><code>&nbsp;29425⭐</code></b> <b><code>&nbsp;&nbsp;2542🍴</code></b> [chromadb](https://github.com/chroma-core/chroma)) - An open-source embedding database for building AI applications with embeddings and semantic search.
  - <b><code>&nbsp;16053⭐</code></b> <b><code>&nbsp;&nbsp;1008🍴</code></b> [zvec](https://github.com/alibaba/zvec)) - A lightweight, in-process vector database that embeds directly into applications.
- Key-Value & Document
  - <b><code>&nbsp;&nbsp;7572⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;634🍴</code></b> [tinydb](https://github.com/msiemens/tinydb)) - A tiny, document-oriented database.

### Caching

_Libraries for caching data._

- <b><code>&nbsp;&nbsp;2782⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;218🍴</code></b> [cachetools](https://github.com/tkem/cachetools)) - Extensible memoizing collections and decorators.
- <b><code>&nbsp;&nbsp;2912⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;190🍴</code></b> [diskcache](https://github.com/grantjenks/python-diskcache)) - SQLite and file backed cache backend, compatible with Django.
- <b><code>&nbsp;&nbsp;&nbsp;413⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;53🍴</code></b> [hishel](https://github.com/karpetrosyan/hishel)) - RFC 9111 compliant HTTP caching for clients like httpx and requests and servers like FastAPI, with sync and async support.
- <b><code>&nbsp;&nbsp;2272⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;242🍴</code></b> [django-cacheops](https://github.com/Suor/django-cacheops)) - A slick ORM cache with automatic granular event-driven invalidation.
- <b><code>&nbsp;&nbsp;&nbsp;299⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;50🍴</code></b> [dogpile.cache](https://github.com/sqlalchemy/dogpile.cache)) - dogpile.cache is a next generation replacement for Beaker made by the same authors.

### Search

_Libraries and software for indexing and performing search queries on data._

- <b><code>&nbsp;&nbsp;&nbsp;470⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;248🍴</code></b> [opensearch-py](https://github.com/opensearch-project/opensearch-py)) - The official low-level Python client for 🌎 [OpenSearch](opensearch.org/).
- <b><code>&nbsp;&nbsp;4388⭐</code></b> <b><code>&nbsp;&nbsp;1222🍴</code></b> [elasticsearch](https://github.com/elastic/elasticsearch-py)) - The official low-level Python client for 🌎 [Elasticsearch](www.elastic.co/elasticsearch).
- <b><code>&nbsp;&nbsp;&nbsp;604⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [meilisearch](https://github.com/meilisearch/meilisearch-python)) - The official Python client for the 🌎 [Meilisearch](www.meilisearch.com/) search engine.
- <b><code>&nbsp;&nbsp;3725⭐</code></b> <b><code>&nbsp;&nbsp;1313🍴</code></b> [django-haystack](https://github.com/django-haystack/django-haystack)) - Modular search for Django.

### Serialization

_Libraries for serializing complex data types._

- <b><code>&nbsp;&nbsp;2107⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;262🍴</code></b> [msgpack](https://github.com/msgpack/msgpack-python)) - MessagePack serializer implementation for Python.
- <b><code>&nbsp;&nbsp;8241⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;335🍴</code></b> [orjson](https://github.com/ijl/orjson)) - Fast, correct JSON library.
- <b><code>&nbsp;&nbsp;7242⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;751🍴</code></b> [marshmallow](https://github.com/marshmallow-code/marshmallow)) - A lightweight library for converting complex objects to and from simple Python datatypes.
- <b><code>&nbsp;&nbsp;4142⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;201🍴</code></b> [msgspec](https://github.com/msgspec/msgspec)) - A fast serialization and validation library with built-in support for JSON, MessagePack, YAML, and TOML.

**Data & Science**

### Data Analysis

_Libraries for data analysis._

- <b><code>&nbsp;49893⭐</code></b> <b><code>&nbsp;20453🍴</code></b> [pandas](https://github.com/pandas-dev/pandas)) - A library providing high-performance, easy-to-use data structures and data analysis tools.
- <b><code>&nbsp;39910⭐</code></b> <b><code>&nbsp;&nbsp;3146🍴</code></b> [polars](https://github.com/pola-rs/polars)) - A fast DataFrame library implemented in Rust with a Python API.
- <b><code>&nbsp;&nbsp;6671⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;768🍴</code></b> [ibis-framework](https://github.com/ibis-project/ibis)) - A portable Python dataframe library with a single API for 20+ backends.

### Data Ingestion / ETL

_Libraries for data extraction, transformation, and loading pipelines across multiple sources and destinations._

- General
  - <b><code>&nbsp;&nbsp;4120⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;750🍴</code></b> [awswrangler](https://github.com/aws/aws-sdk-pandas)) - Pandas integration with AWS services like Athena, Glue, Redshift, S3, and DynamoDB.
  - <b><code>&nbsp;&nbsp;5924⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;616🍴</code></b> [dlt](https://github.com/dlt-hub/dlt)) - A Python library for building data pipelines with automatic schema inference, incremental loading, and support for multiple sources and destinations.
- Financial Data
  - <b><code>&nbsp;25413⭐</code></b> <b><code>&nbsp;&nbsp;3435🍴</code></b> [yfinance](https://github.com/ranaroussi/yfinance)) - Easy Pythonic way to download market and financial data from Yahoo Finance.
  - <b><code>&nbsp;22813⭐</code></b> <b><code>&nbsp;&nbsp;3528🍴</code></b> [akshare](https://github.com/akfamily/akshare)) - A financial data interface library, with data provided for academic research only.
  - <b><code>&nbsp;&nbsp;2760⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;498🍴</code></b> [edgartools](https://github.com/dgunning/edgartools)) - Library for downloading structured data from SEC EDGAR filings and XBRL financial statements.
  - <b><code>&nbsp;73752⭐</code></b> <b><code>&nbsp;&nbsp;7639🍴</code></b> [openbb](https://github.com/openbq-org/OpenBB)) - A financial data platform for analysts, quants and AI agents.

### Data Validation

_Libraries for validating data._

- <b><code>&nbsp;28919⭐</code></b> <b><code>&nbsp;&nbsp;3010🍴</code></b> [pydantic](https://github.com/pydantic/pydantic)) - Data validation using Python type hints.
- <b><code>&nbsp;&nbsp;4988⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;687🍴</code></b> [jsonschema](https://github.com/python-jsonschema/jsonschema)) - An implementation of 🌎 [JSON Schema](json-schema.org/) for Python.
- <b><code>&nbsp;11854⭐</code></b> <b><code>&nbsp;&nbsp;1866🍴</code></b> [great-expectations](https://github.com/fivetran/great_expectations)) - A data quality framework for validating, documenting, and profiling data with declarative expectations.
- <b><code>&nbsp;&nbsp;4472⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;465🍴</code></b> [pandera](https://github.com/unionai-oss/pandera)) - A data validation library for dataframes, with support for pandas, polars, PySpark, and more.

### Data Visualization

_Libraries for visualizing data. Also see <b><code>&nbsp;35032⭐</code></b> <b><code>&nbsp;&nbsp;4559🍴</code></b> [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization))._

- Plotting
  - <b><code>&nbsp;23314⭐</code></b> <b><code>&nbsp;&nbsp;8497🍴</code></b> [matplotlib](https://github.com/matplotlib/matplotlib)) - A comprehensive library for creating static, animated, and interactive visualizations.
  - <b><code>&nbsp;18818⭐</code></b> <b><code>&nbsp;&nbsp;2858🍴</code></b> [plotly](https://github.com/plotly/plotly.py)) - Interactive graphing library for Python.
  - <b><code>&nbsp;14054⭐</code></b> <b><code>&nbsp;&nbsp;2144🍴</code></b> [seaborn](https://github.com/mwaskom/seaborn)) - Statistical data visualization using Matplotlib.
  - <b><code>&nbsp;10488⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;873🍴</code></b> [altair](https://github.com/vega/altair)) - Declarative statistical visualization library for Python.
  - <b><code>&nbsp;20456⭐</code></b> <b><code>&nbsp;&nbsp;4265🍴</code></b> [bokeh](https://github.com/bokeh/bokeh)) - Interactive Web Plotting for Python.
- Specialized
  - <b><code>&nbsp;&nbsp;1814⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;220🍴</code></b> [graphviz](https://github.com/xflr6/graphviz)) - Simple Python interface for creating and rendering Graphviz graphs.
  - <b><code>&nbsp;&nbsp;1621⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;400🍴</code></b> [cartopy](https://github.com/SciTools/cartopy)) - A cartographic python library with matplotlib support.
  - <b><code>123180⭐</code></b> <b><code>&nbsp;11877🍴</code></b> [graphify](https://github.com/Graphify-Labs/graphify)) - Turn any folder of code, SQL schemas, docs, papers, images, or videos into a queryable knowledge graph.
- Dashboards and Apps
  - <b><code>&nbsp;45872⭐</code></b> <b><code>&nbsp;&nbsp;4406🍴</code></b> [streamlit](https://github.com/streamlit/streamlit)) - A framework which lets you build dashboards, generate reports, or create chat apps in minutes.
  - <b><code>&nbsp;24441⭐</code></b> <b><code>&nbsp;&nbsp;2328🍴</code></b> [dash](https://github.com/plotly/dash)) - A framework for building data apps and dashboards in pure Python, built on Plotly.
  - <b><code>&nbsp;43654⭐</code></b> <b><code>&nbsp;&nbsp;3616🍴</code></b> [gradio](https://github.com/gradio-app/gradio)) - Build and share machine learning apps, all in Python.

### Geolocation

_Libraries for geocoding addresses and working with latitudes and longitudes._

- <b><code>&nbsp;&nbsp;5272⭐</code></b> <b><code>&nbsp;&nbsp;1063🍴</code></b> [geopandas](https://github.com/geopandas/geopandas)) - Python tools for geographic data (GeoSeries/GeoDataFrame) built on pandas.
- <b><code>&nbsp;&nbsp;4867⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;668🍴</code></b> [geopy](https://github.com/geopy/geopy)) - Python Geocoding Toolbox.
- <b><code>&nbsp;&nbsp;&nbsp;997⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;137🍴</code></b> [geojson](https://github.com/jazzband/geojson)) - Python bindings and utilities for GeoJSON.
- <b><code>&nbsp;91241⭐</code></b> <b><code>&nbsp;35936🍴</code></b> [geodjango](https://github.com/django/django)) - (part of Django) A world-class 🌎 [geographic web framework](docs.djangoproject.com/en/stable/ref/contrib/gis/).

### Science

_Libraries for scientific computing. Also see <b><code>&nbsp;&nbsp;&nbsp;376⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;48🍴</code></b> [Python-for-Scientists](https://github.com/TomNicholas/Python-for-Scientists))._

- Core
  - <b><code>&nbsp;32898⭐</code></b> <b><code>&nbsp;12866🍴</code></b> [numpy](https://github.com/numpy/numpy)) - A fundamental package for scientific computing with Python.
  - <b><code>&nbsp;15070⭐</code></b> <b><code>&nbsp;&nbsp;5982🍴</code></b> [scipy](https://github.com/scipy/scipy)) - Fundamental algorithms for scientific computing in Python.
  - <b><code>&nbsp;11169⭐</code></b> <b><code>&nbsp;&nbsp;1334🍴</code></b> [numba](https://github.com/numba/numba)) - A NumPy-aware JIT compiler for Python, using LLVM.
- Symbolic Mathematics
  - <b><code>&nbsp;14987⭐</code></b> <b><code>&nbsp;&nbsp;5546🍴</code></b> [sympy](https://github.com/sympy/sympy)) - A Python library for symbolic mathematics.
- Statistics
  - <b><code>&nbsp;11670⭐</code></b> <b><code>&nbsp;&nbsp;3611🍴</code></b> [statsmodels](https://github.com/statsmodels/statsmodels)) - Statistical modeling and econometrics in Python.
- Biology and Chemistry
  - <b><code>&nbsp;&nbsp;3603⭐</code></b> <b><code>&nbsp;&nbsp;1071🍴</code></b> [rdkit](https://github.com/rdkit/rdkit)) - Cheminformatics and Machine Learning Software.
  - <b><code>&nbsp;&nbsp;5218⭐</code></b> <b><code>&nbsp;&nbsp;1961🍴</code></b> [biopython](https://github.com/biopython/biopython)) - Biopython is a set of freely available tools for biological computation.
- Physics and Engineering
  - <b><code>&nbsp;&nbsp;2808⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;545🍴</code></b> [pint](https://github.com/hgrecco/pint)) - Operate and manipulate physical quantities with units and dimensional analysis.
  - <b><code>&nbsp;&nbsp;5323⭐</code></b> <b><code>&nbsp;&nbsp;2188🍴</code></b> [astropy](https://github.com/astropy/astropy)) - A community Python library for Astronomy.
  - <b><code>&nbsp;&nbsp;1337⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;568🍴</code></b> [obspy](https://github.com/obspy/obspy)) - A Python toolbox for seismology.
- Simulation and Modeling
  - <b><code>&nbsp;&nbsp;9790⭐</code></b> <b><code>&nbsp;&nbsp;2315🍴</code></b> [pymc](https://github.com/pymc-devs/pymc)) - Probabilistic programming and Bayesian modeling in Python.
  - 🌎 [simpy](gitlab.com/team-simpy/simpy) - A process-based discrete-event simulation framework.
  - <b><code>&nbsp;&nbsp;3871⭐</code></b> <b><code>&nbsp;&nbsp;1321🍴</code></b> [mesa](https://github.com/mesa/mesa)) - An agent-based modeling framework for building, analyzing, and visualizing complex system simulations.
- Graphs and Networks
  - <b><code>&nbsp;17305⭐</code></b> <b><code>&nbsp;&nbsp;3626🍴</code></b> [networkx](https://github.com/networkx/networkx)) - A high-productivity software for complex networks.
- Computational Geometry
  - <b><code>&nbsp;&nbsp;4516⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;637🍴</code></b> [shapely](https://github.com/shapely/shapely)) - Manipulation and analysis of geometric objects in the Cartesian plane.
- Other
  - <b><code>&nbsp;&nbsp;2661⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;294🍴</code></b> [colour-science](https://github.com/colour-science/colour)) - Implementing a comprehensive number of colour theory transformations and algorithms.
  - <b><code>&nbsp;41184⭐</code></b> <b><code>&nbsp;&nbsp;3141🍴</code></b> [manim](https://github.com/ManimCommunity/manim)) - An animation engine for explanatory math videos.

### Quantum Computing

_Libraries for quantum computing._

- <b><code>&nbsp;&nbsp;7851⭐</code></b> <b><code>&nbsp;&nbsp;3066🍴</code></b> [qiskit](https://github.com/Qiskit/qiskit)) - An IBM-backed quantum SDK for building, simulating, and running circuits on real quantum hardware.
- <b><code>&nbsp;&nbsp;2081⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;794🍴</code></b> [qutip](https://github.com/qutip/qutip)) - Quantum Toolbox in Python.
- <b><code>&nbsp;&nbsp;3483⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;873🍴</code></b> [pennylane](https://github.com/PennyLaneAI/pennylane)) - A cross-platform library for quantum computing, quantum machine learning, and quantum chemistry.
- <b><code>&nbsp;&nbsp;5077⭐</code></b> <b><code>&nbsp;&nbsp;1282🍴</code></b> [cirq](https://github.com/quantumlib/Cirq)) - A Google-developed framework focused on hardware-aware quantum circuit design for NISQ devices.

**Developer Tools**

### Algorithms and Design Patterns

_Python implementation of data structures, algorithms and design patterns. Also see <b><code>&nbsp;25597⭐</code></b> <b><code>&nbsp;&nbsp;2965🍴</code></b> [awesome-algorithms](https://github.com/tayllan/awesome-algorithms))._

- Algorithms
  - <b><code>&nbsp;&nbsp;3981⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;238🍴</code></b> [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)) - Fast and pure-Python implementation of sorted collections.
  - <b><code>&nbsp;25559⭐</code></b> <b><code>&nbsp;&nbsp;4708🍴</code></b> [algorithms](https://github.com/keon/algorithms)) - Minimal examples of data structures and algorithms.
  - <b><code>225204⭐</code></b> <b><code>&nbsp;51152🍴</code></b> [thealgorithms](https://github.com/TheAlgorithms/Python)) - All Algorithms implemented in Python.
- Design Patterns
  - <b><code>&nbsp;43029⭐</code></b> <b><code>&nbsp;&nbsp;6986🍴</code></b> [python-patterns](https://github.com/faif/python-patterns)) - A collection of design patterns and idioms in Python.
  - <b><code>&nbsp;&nbsp;1319⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;116🍴</code></b> [python-statemachine](https://github.com/fgmacedo/python-statemachine)) - Expressive statecharts and finite state machines with a declarative API, in sync and async codebases.

### Interactive Interpreter

_Interactive Python interpreters (REPL)._

- <b><code>&nbsp;16786⭐</code></b> <b><code>&nbsp;&nbsp;4525🍴</code></b> [ipython](https://github.com/ipython/ipython)) - A powerful interactive Python shell, and the kernel behind Jupyter notebooks.
- <b><code>&nbsp;13408⭐</code></b> <b><code>&nbsp;&nbsp;5782🍴</code></b> [notebook](https://github.com/jupyter/notebook)) - A web-based notebook environment for interactive computing.
  - <b><code>&nbsp;&nbsp;4678⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;462🍴</code></b> [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter))
- <b><code>&nbsp;22988⭐</code></b> <b><code>&nbsp;&nbsp;1309🍴</code></b> [marimo](https://github.com/marimo-team/marimo)) - A reactive notebook for Python, stored as pure Python and runnable as a script or app.
- <b><code>&nbsp;&nbsp;5457⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;293🍴</code></b> [ptpython](https://github.com/prompt-toolkit/ptpython)) - Advanced Python REPL built on top of the <b><code>&nbsp;10593⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;821🍴</code></b> [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)).

### Code Analysis

_Tools of static analysis, linters and code quality checkers. Also see <b><code>&nbsp;14819⭐</code></b> <b><code>&nbsp;&nbsp;1514🍴</code></b> [awesome-static-analysis](https://github.com/analysis-tools-dev/static-analysis))._

- Code Analysis
  - <b><code>&nbsp;&nbsp;1203⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;87🍴</code></b> [import-linter](https://github.com/seddonym/import-linter)) - A linter that enforces architectural constraints on imports between Python modules.
  - <b><code>&nbsp;&nbsp;4831⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;203🍴</code></b> [vulture](https://github.com/jendrikseipp/vulture)) - A tool for finding and analyzing dead Python code.
  - <b><code>&nbsp;&nbsp;&nbsp;869⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;26🍴</code></b> [complexipy](https://github.com/rohaquinlop/complexipy)) - Cognitive complexity analysis for Python code, written in Rust.
  - <b><code>&nbsp;&nbsp;2084⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;180🍴</code></b> [prospector](https://github.com/prospector-dev/prospector)) - A tool to analyze Python code.
- Git Hooks
  - <b><code>&nbsp;15606⭐</code></b> <b><code>&nbsp;&nbsp;1012🍴</code></b> [pre-commit](https://github.com/pre-commit/pre-commit)) - A framework for managing and maintaining multi-language pre-commit hooks.
- Linters and Formatters
  - <b><code>&nbsp;49878⭐</code></b> <b><code>&nbsp;&nbsp;2460🍴</code></b> [ruff](https://github.com/astral-sh/ruff)) - An extremely fast Python linter and code formatter.
  - <b><code>&nbsp;41857⭐</code></b> <b><code>&nbsp;&nbsp;2903🍴</code></b> [black](https://github.com/psf/black)) - The uncompromising Python code formatter.
  - <b><code>&nbsp;&nbsp;6960⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;703🍴</code></b> [isort](https://github.com/PyCQA/isort)) - A Python utility / library to sort imports.
  - <b><code>&nbsp;&nbsp;5729⭐</code></b> <b><code>&nbsp;&nbsp;1362🍴</code></b> [pylint](https://github.com/pylint-dev/pylint)) - A fully customizable source code analyzer.
  - <b><code>&nbsp;&nbsp;3825⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;364🍴</code></b> [flake8](https://github.com/PyCQA/flake8)) - A wrapper around `pycodestyle`, `pyflakes` and McCabe.
    - <b><code>&nbsp;&nbsp;1283⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;51🍴</code></b> [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions))
  - <b><code>&nbsp;&nbsp;8289⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;844🍴</code></b> [bandit](https://github.com/PyCQA/bandit)) - A tool designed to find common security issues in Python code.
- Refactoring
  - <b><code>&nbsp;&nbsp;2239⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;197🍴</code></b> [rope](https://github.com/python-rope/rope)) - Rope is a python refactoring library.
- Type Checkers - <b><code>&nbsp;&nbsp;1987⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;78🍴</code></b> [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing))
  - <b><code>&nbsp;20652⭐</code></b> <b><code>&nbsp;&nbsp;3320🍴</code></b> [mypy](https://github.com/python/mypy)) - A static type checker for Python.
  - <b><code>&nbsp;19786⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;336🍴</code></b> [ty](https://github.com/astral-sh/ty)) - An extremely fast Python type checker and language server.
  - <b><code>&nbsp;15670⭐</code></b> <b><code>&nbsp;&nbsp;1818🍴</code></b> [pyright](https://github.com/microsoft/pyright)) - Full-featured static type checker for Python from Microsoft, the engine behind Pylance.
  - <b><code>&nbsp;&nbsp;7039⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;530🍴</code></b> [pyrefly](https://github.com/facebook/pyrefly)) - A fast type checker and language server for Python.

### Testing

_Libraries for testing codebases and generating test data. Also see <b><code>&nbsp;&nbsp;&nbsp;311⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;58🍴</code></b> [awesome-python-testing](https://github.com/cleder/awesome-python-testing))._

- Frameworks
  - <b><code>&nbsp;14558⭐</code></b> <b><code>&nbsp;&nbsp;3433🍴</code></b> [pytest](https://github.com/pytest-dev/pytest)) - A mature full-featured Python testing tool.
    - <b><code>&nbsp;&nbsp;&nbsp;575⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;67🍴</code></b> [awesome-pytest](https://github.com/augustogoulart/awesome-pytest))
  - <b><code>&nbsp;&nbsp;9037⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;686🍴</code></b> [hypothesis](https://github.com/HypothesisWorks/hypothesis)) - Hypothesis is an advanced Quickcheck style property based testing library.
  - <b><code>&nbsp;11923⭐</code></b> <b><code>&nbsp;&nbsp;2566🍴</code></b> [robotframework](https://github.com/robotframework/robotframework)) - A generic test automation framework.
- Test Runners
  - <b><code>&nbsp;&nbsp;3942⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;595🍴</code></b> [tox](https://github.com/tox-dev/tox)) - Auto builds and tests distributions in multiple Python versions.
  - <b><code>&nbsp;&nbsp;1562⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;199🍴</code></b> [nox](https://github.com/wntrblm/nox)) - Flexible test automation for Python.
- Browser Automation
  - <b><code>&nbsp;15023⭐</code></b> <b><code>&nbsp;&nbsp;1239🍴</code></b> [playwright-python](https://github.com/microsoft/playwright-python)) - Python version of the Playwright testing and automation library.
  - <b><code>&nbsp;34518⭐</code></b> <b><code>&nbsp;&nbsp;8718🍴</code></b> [selenium](https://github.com/SeleniumHQ/selenium)) - Python bindings for 🌎 [Selenium](selenium.dev/) 🌎 [WebDriver](selenium.dev/documentation/webdriver/).
  - <b><code>&nbsp;13048⭐</code></b> <b><code>&nbsp;&nbsp;1592🍴</code></b> [seleniumbase](https://github.com/seleniumbase/SeleniumBase)) - Python framework for web automation & testing, with stealth options.
- Load Testing
  - <b><code>&nbsp;28195⭐</code></b> <b><code>&nbsp;&nbsp;3253🍴</code></b> [locust](https://github.com/locustio/locust)) - Scalable user load testing tool written in Python.
- API Testing
  - <b><code>&nbsp;&nbsp;3644⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;226🍴</code></b> [schemathesis](https://github.com/schemathesis/schemathesis)) - A tool for automatic property-based testing of web APIs from OpenAPI or GraphQL schemas.
- Mock
  - 🌎 [unittest.mock](docs.python.org/3/library/unittest.mock.html) - (Python standard library) A mocking and patching library.
  - <b><code>&nbsp;&nbsp;4343⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;385🍴</code></b> [responses](https://github.com/getsentry/responses)) - A utility library for mocking out the requests Python library.
  - <b><code>&nbsp;&nbsp;3019⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;444🍴</code></b> [vcrpy](https://github.com/kevin1024/vcrpy)) - Record and replay HTTP interactions on your tests.
  - <b><code>&nbsp;&nbsp;&nbsp;837⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;65🍴</code></b> [respx](https://github.com/lundberg/respx)) - Mock HTTPX with awesome request patterns and response side effects.
  - <b><code>&nbsp;&nbsp;1010⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;55🍴</code></b> [time-machine](https://github.com/adamchainz/time-machine)) - Travel through time in your tests by mocking the current time at the C level.
- Object Factories
  - <b><code>&nbsp;&nbsp;3812⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;424🍴</code></b> [factory-boy](https://github.com/FactoryBoy/factory_boy)) - A test fixtures replacement for Python.
  - <b><code>&nbsp;&nbsp;1512⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;121🍴</code></b> [polyfactory](https://github.com/litestar-org/polyfactory)) - A mock data generation library based on type hints (continuation of `pydantic-factories`).
- Code Coverage
  - <b><code>&nbsp;&nbsp;3410⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;539🍴</code></b> [coverage](https://github.com/coveragepy/coveragepy)) - Code coverage measurement.
- Fake Data
  - <b><code>&nbsp;19424⭐</code></b> <b><code>&nbsp;&nbsp;2123🍴</code></b> [faker](https://github.com/joke2k/faker)) - A Python package that generates fake data.
  - <b><code>&nbsp;&nbsp;4841⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;364🍴</code></b> [mimesis](https://github.com/lk-geimfari/mimesis)) - A Python library for generating fake but realistic data in multiple languages and locales.

### Debugging Tools

_Libraries for debugging code._

- pdb-like Debugger
  - <b><code>&nbsp;&nbsp;1975⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;153🍴</code></b> [ipdb](https://github.com/gotcha/ipdb)) - IPython-enabled 🌎 [pdb](docs.python.org/3/library/pdb.html).
  - <b><code>&nbsp;&nbsp;3247⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;245🍴</code></b> [pudb](https://github.com/inducer/pudb)) - A full-screen, console-based Python debugger.
- Tracing
  - <b><code>&nbsp;&nbsp;7751⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;476🍴</code></b> [viztracer](https://github.com/gaogaotiantian/viztracer)) - A low-overhead tool that traces and visualizes Python code execution.
- Profiler
  - <b><code>&nbsp;15531⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;552🍴</code></b> [py-spy](https://github.com/benfred/py-spy)) - A sampling profiler for Python programs. Written in Rust.
  - <b><code>&nbsp;15251⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;469🍴</code></b> [memray](https://github.com/bloomberg/memray)) - A memory profiler that tracks allocations in Python code, native extensions, and the interpreter itself.
  - <b><code>&nbsp;&nbsp;8014⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;302🍴</code></b> [pyinstrument](https://github.com/joerick/pyinstrument)) - A statistical wall-clock profiler with low overhead and readable call-tree output.
  - <b><code>&nbsp;13522⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;440🍴</code></b> [scalene](https://github.com/plasma-umass/scalene)) - A high-performance, high-precision CPU, GPU, and memory profiler for Python.
- Others
  - <b><code>&nbsp;&nbsp;8380⭐</code></b> <b><code>&nbsp;&nbsp;1108🍴</code></b> [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar)) - Display various debug information for Django.
  - <b><code>&nbsp;10112⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;234🍴</code></b> [icecream](https://github.com/gruns/icecream)) - Inspect variables, expressions, and program execution with a single, simple function call.
  - <b><code>&nbsp;&nbsp;&nbsp;978⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;154🍴</code></b> [flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar)) - A port of the django-debug-toolbar to flask.

### Build Tools

_Task runners and software build tools. If you're looking for Python packaging/build tools, see [Package Management](#package-management)._

- <b><code>&nbsp;&nbsp;4780⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;414🍴</code></b> [invoke](https://github.com/pyinvoke/invoke)) - A tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks.
- <b><code>&nbsp;&nbsp;2087⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;78🍴</code></b> [poethepoet](https://github.com/nat-n/poethepoet)) - A task runner that defines tasks in pyproject.toml and works with poetry or uv.
- <b><code>&nbsp;&nbsp;2427⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;361🍴</code></b> [scons](https://github.com/SCons/scons)) - A software construction tool.
- <b><code>&nbsp;&nbsp;2088⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;199🍴</code></b> [doit](https://github.com/pydoit/doit)) - A task runner and build tool.

### Documentation

_Libraries for generating project documentation._

- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [sphinx](https://github.com/sphinx-doc/sphinx/)) - Python Documentation generator.
  - <b><code>&nbsp;&nbsp;&nbsp;978⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;78🍴</code></b> [awesome-sphinxdoc](https://github.com/ygzgxyz/awesome-sphinxdoc))
- <b><code>&nbsp;27530⭐</code></b> <b><code>&nbsp;&nbsp;4148🍴</code></b> [mkdocs-material](https://github.com/squidfunk/mkdocs-material)) - A documentation framework and Material Design theme built on MkDocs.
- <b><code>&nbsp;42667⭐</code></b> <b><code>&nbsp;&nbsp;2733🍴</code></b> [diagrams](https://github.com/mingrammer/diagrams)) - Diagram as Code.
- <b><code>&nbsp;&nbsp;2514⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;232🍴</code></b> [pdoc](https://github.com/mitmproxy/pdoc)) - Auto-generates API documentation for Python projects.
- <b><code>&nbsp;&nbsp;5818⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;132🍴</code></b> [zensical](https://github.com/zensical/zensical)) - A modern static site generator for technical documentation.

**DevOps**

### DevOps Tools

_Software and libraries for DevOps._

- Cloud Providers
  - <b><code>&nbsp;&nbsp;9912⭐</code></b> <b><code>&nbsp;&nbsp;1996🍴</code></b> [boto3](https://github.com/boto/boto3)) - Python interface to Amazon Web Services.
  - <b><code>&nbsp;17284⭐</code></b> <b><code>&nbsp;&nbsp;4716🍴</code></b> [awscli](https://github.com/aws/aws-cli)) - Universal Command Line Interface for Amazon Web Services; the PyPI package is v1, in maintenance mode, while v2 ships as AWS's bundled installer.
  - <b><code>&nbsp;&nbsp;5612⭐</code></b> <b><code>&nbsp;&nbsp;3378🍴</code></b> [azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python)) - Microsoft Azure SDK for Python, published as per-service packages.
  - <b><code>&nbsp;&nbsp;5395⭐</code></b> <b><code>&nbsp;&nbsp;1787🍴</code></b> [google-cloud-python](https://github.com/googleapis/google-cloud-python)) - Google Cloud client libraries for Python, published as per-service packages.
- Configuration Management
  - <b><code>&nbsp;70826⭐</code></b> <b><code>&nbsp;24337🍴</code></b> [ansible](https://github.com/ansible/ansible)) - A radically simple IT automation platform.
  - <b><code>&nbsp;&nbsp;3826⭐</code></b> <b><code>&nbsp;&nbsp;1158🍴</code></b> [cloud-init](https://github.com/canonical/cloud-init)) - A multi-distribution package that handles early initialization of a cloud instance.
  - <b><code>&nbsp;&nbsp;6025⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;552🍴</code></b> [pyinfra](https://github.com/pyinfra-dev/pyinfra)) - Turns Python code into shell commands and runs them on your servers.
  - <b><code>&nbsp;15687⭐</code></b> <b><code>&nbsp;&nbsp;5610🍴</code></b> [salt](https://github.com/saltstack/salt)) - Infrastructure automation and management system.
- Deployment
  - <b><code>&nbsp;15508⭐</code></b> <b><code>&nbsp;&nbsp;1953🍴</code></b> [fabric](https://github.com/fabric/fabric)) - A simple, Pythonic tool for remote execution and deployment.
  - <b><code>&nbsp;11052⭐</code></b> <b><code>&nbsp;&nbsp;1013🍴</code></b> [chalice](https://github.com/aws/chalice)) - A Python serverless microframework for AWS.
- Monitoring and Processes
  - <b><code>&nbsp;11286⭐</code></b> <b><code>&nbsp;&nbsp;1521🍴</code></b> [psutil](https://github.com/giampaolo/psutil)) - A cross-platform process and system utilities module.
  - <b><code>&nbsp;&nbsp;2209⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;680🍴</code></b> [sentry-sdk](https://github.com/getsentry/sentry-python)) - Sentry SDK for Python.
  - <b><code>&nbsp;&nbsp;9124⭐</code></b> <b><code>&nbsp;&nbsp;1268🍴</code></b> [supervisor](https://github.com/Supervisor/supervisor)) - Supervisor process control system for UNIX.
  - <b><code>&nbsp;&nbsp;7242⭐</code></b> <b><code>&nbsp;&nbsp;1153🍴</code></b> [flower](https://github.com/mher/flower)) - A real-time monitor and web admin for Celery task queues.
  - <b><code>&nbsp;&nbsp;7245⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;504🍴</code></b> [sh](https://github.com/amoffat/sh)) - A full-fledged subprocess replacement for Python.
- Other
  - <b><code>&nbsp;13797⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;875🍴</code></b> [borgbackup](https://github.com/borgbackup/borg)) - A deduplicating archiver with compression and encryption.

### Distributed Computing

_Frameworks and libraries for Distributed Computing._

- <b><code>&nbsp;44107⭐</code></b> <b><code>&nbsp;29399🍴</code></b> [pyspark](https://github.com/apache/spark)) - 🌎 [Apache Spark](spark.apache.org/) Python API.
- <b><code>&nbsp;13928⭐</code></b> <b><code>&nbsp;&nbsp;1971🍴</code></b> [dask](https://github.com/dask/dask)) - A flexible parallel computing library for analytic computing.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [ray](https://github.com/ray-project/ray/)) - A unified framework for scaling AI and Python applications.
- <b><code>&nbsp;&nbsp;4398⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;488🍴</code></b> [joblib](https://github.com/joblib/joblib)) - Parallel computing and disk-based caching for Python functions.
- <b><code>&nbsp;&nbsp;&nbsp;926⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;137🍴</code></b> [mpi4py](https://github.com/mpi4py/mpi4py)) - Python bindings for MPI.

### Task Queues

_Libraries for working with task queues._

- <b><code>&nbsp;28929⭐</code></b> <b><code>&nbsp;&nbsp;5195🍴</code></b> [celery](https://github.com/celery/celery)) - An asynchronous task queue/job queue based on distributed message passing.
- <b><code>&nbsp;10695⭐</code></b> <b><code>&nbsp;&nbsp;1501🍴</code></b> [rq](https://github.com/rq/rq)) - Simple job queues for Python.
- <b><code>&nbsp;&nbsp;5322⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;385🍴</code></b> [dramatiq](https://github.com/Bogdanp/dramatiq)) - A fast and reliable background task processing library for Python 3.
- <b><code>&nbsp;&nbsp;6039⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;402🍴</code></b> [huey](https://github.com/coleifer/huey)) - A little task queue with multi-process, multi-thread, or greenlet workers.
- <b><code>&nbsp;&nbsp;2345⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;148🍴</code></b> [taskiq](https://github.com/taskiq-python/taskiq)) - Distributed task queue with native asyncio support and pluggable brokers.

### Messaging

_Libraries for working with message brokers and event streaming._

- <b><code>&nbsp;&nbsp;&nbsp;515⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;967🍴</code></b> [confluent-kafka](https://github.com/confluentinc/confluent-kafka-python)) - Confluent's Python client for Apache Kafka, built on librdkafka.
- <b><code>&nbsp;&nbsp;3888⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;855🍴</code></b> [pika](https://github.com/pika/pika)) - Pure-Python RabbitMQ/AMQP 0-9-1 client library.
- <b><code>&nbsp;&nbsp;2428⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;750🍴</code></b> [paho-mqtt](https://github.com/eclipse-paho/paho.mqtt.python)) - The Eclipse Paho MQTT client for Python.
- <b><code>&nbsp;&nbsp;5358⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;408🍴</code></b> [faststream](https://github.com/ag2ai/faststream)) - A framework for building asynchronous services over Apache Kafka, RabbitMQ, NATS, MQTT and Redis.

### Job Schedulers

_Libraries for scheduling jobs._

- Task Scheduling
  - <b><code>&nbsp;&nbsp;7643⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;797🍴</code></b> [apscheduler](https://github.com/agronholm/apscheduler)) - A light but powerful in-process task scheduler that lets you schedule functions.
  - <b><code>&nbsp;12276⭐</code></b> <b><code>&nbsp;&nbsp;1005🍴</code></b> [schedule](https://github.com/dbader/schedule)) - Python job scheduling for humans.
- Workflow Orchestration
  - <b><code>&nbsp;16231⭐</code></b> <b><code>&nbsp;&nbsp;2321🍴</code></b> [dagster](https://github.com/dagster-io/dagster)) - An orchestration platform for the development, production, and observation of data assets.
  - <b><code>&nbsp;47032⭐</code></b> <b><code>&nbsp;17939🍴</code></b> [apache-airflow](https://github.com/apache/airflow)) - Airflow is a platform to programmatically author, schedule and monitor workflows.
  - <b><code>&nbsp;23964⭐</code></b> <b><code>&nbsp;&nbsp;2551🍴</code></b> [prefect](https://github.com/PrefectHQ/prefect)) - A modern workflow orchestration framework that makes it easy to build, schedule and monitor robust data pipelines.

### Logging

_Libraries for generating and working with logs._

- 🌎 [logging](docs.python.org/3/library/logging.html) - (Python standard library) Logging facility for Python.
- <b><code>&nbsp;&nbsp;4968⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;303🍴</code></b> [structlog](https://github.com/hynek/structlog)) - Structured logging made easy.
- <b><code>&nbsp;24139⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;824🍴</code></b> [loguru](https://github.com/Delgan/loguru)) - Library which aims to bring enjoyable logging in Python.
- <b><code>&nbsp;&nbsp;4503⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;302🍴</code></b> [logfire](https://github.com/pydantic/logfire)) - The observability platform for Python, from the makers of Pydantic.

### Network Virtualization

_Tools and libraries for packet manipulation and network device automation._

- <b><code>&nbsp;12578⭐</code></b> <b><code>&nbsp;&nbsp;2264🍴</code></b> [scapy](https://github.com/secdev/scapy)) - A brilliant packet manipulation library.
- <b><code>&nbsp;&nbsp;4300⭐</code></b> <b><code>&nbsp;&nbsp;1387🍴</code></b> [netmiko](https://github.com/ktbyers/netmiko)) - Multi-vendor library to simplify CLI connections to network devices.
- <b><code>&nbsp;&nbsp;2507⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;593🍴</code></b> [napalm](https://github.com/napalm-automation/napalm)) - Cross-vendor API to manipulate network devices.

**CLI & GUI**

### CLI Development

_Libraries for building command-line applications._

- CLI Development
  - 🌎 [argparse](docs.python.org/3/library/argparse.html) - (Python standard library) Command-line option and argument parsing.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [click](https://github.com/pallets/click/)) - A package for creating beautiful command line interfaces in a composable way.
  - <b><code>&nbsp;20049⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;982🍴</code></b> [typer](https://github.com/fastapi/typer)) - Modern CLI framework that uses Python type hints. Built on Click.
  - <b><code>&nbsp;10593⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;821🍴</code></b> [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)) - A library for building powerful interactive command lines.
  - <b><code>&nbsp;28225⭐</code></b> <b><code>&nbsp;&nbsp;1493🍴</code></b> [fire](https://github.com/google/python-fire)) - A library for creating command line interfaces from absolutely any Python object.
- Terminal Rendering
  - <b><code>&nbsp;57464⭐</code></b> <b><code>&nbsp;&nbsp;2383🍴</code></b> [rich](https://github.com/Textualize/rich)) - Python library for rich text and beautiful formatting in the terminal. Also provides a great `RichHandler` log handler.
  - <b><code>&nbsp;31351⭐</code></b> <b><code>&nbsp;&nbsp;2825🍴</code></b> [tqdm](https://github.com/tqdm/tqdm)) - Fast, extensible progress bar for loops and CLI.
  - <b><code>&nbsp;&nbsp;3795⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;286🍴</code></b> [colorama](https://github.com/tartley/colorama)) - Cross-platform colored terminal text.
  - <b><code>&nbsp;&nbsp;6311⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;238🍴</code></b> [alive-progress](https://github.com/rsalmei/alive-progress)) - A new kind of Progress Bar, with real-time throughput, eta and very cool animations.
- TUI Frameworks
  - <b><code>&nbsp;37380⭐</code></b> <b><code>&nbsp;&nbsp;1345🍴</code></b> [textual](https://github.com/Textualize/textual)) - A framework for building interactive user interfaces that run in the terminal and the browser.
  - <b><code>&nbsp;&nbsp;3021⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;345🍴</code></b> [urwid](https://github.com/urwid/urwid)) - A library for creating terminal GUI applications with strong support for widgets, events, rich colors, etc.
  - <b><code>&nbsp;&nbsp;4303⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;264🍴</code></b> [asciimatics](https://github.com/peterbrittain/asciimatics)) - A package to create full-screen text UIs (from interactive forms to ASCII animations).

### CLI Tools

_Useful CLI-based tools._

- Database CLIs
  - <b><code>&nbsp;13412⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;612🍴</code></b> [pgcli](https://github.com/dbcli/pgcli)) - PostgreSQL CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;11979⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;696🍴</code></b> [mycli](https://github.com/dbcli/mycli)) - MySQL CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;&nbsp;3310⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;98🍴</code></b> [litecli](https://github.com/dbcli/litecli)) - SQLite CLI with autocompletion and syntax highlighting.
  - <b><code>&nbsp;&nbsp;2760⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;121🍴</code></b> [iredis](https://github.com/laixintao/iredis)) - Redis CLI with autocompletion and syntax highlighting.
- Downloaders
  - <b><code>194880⭐</code></b> <b><code>&nbsp;16939🍴</code></b> [yt-dlp](https://github.com/yt-dlp/yt-dlp)) - A command-line program to download videos from YouTube and other video sites, a fork of youtube-dl.
- HTTP Clients
  - <b><code>&nbsp;38604⭐</code></b> <b><code>&nbsp;&nbsp;4014🍴</code></b> [httpie](https://github.com/httpie/cli)) - A command line HTTP client, a user-friendly cURL replacement.
- Project Scaffolding
  - <b><code>&nbsp;25122⭐</code></b> <b><code>&nbsp;&nbsp;2284🍴</code></b> [cookiecutter](https://github.com/cookiecutter/cookiecutter)) - A command-line utility that creates projects from cookiecutters (project templates).
  - <b><code>&nbsp;&nbsp;3607⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;273🍴</code></b> [copier](https://github.com/copier-org/copier)) - A library and command-line utility for rendering project templates.
- Shells
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [xonsh](https://github.com/xonsh/xonsh/)) - A Python-powered shell. Full-featured and cross-platform.
- Terminal Workflow
  - <b><code>&nbsp;&nbsp;4588⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;247🍴</code></b> [tmuxp](https://github.com/tmux-python/tmuxp)) - A <b><code>&nbsp;49620⭐</code></b> <b><code>&nbsp;&nbsp;2924🍴</code></b> [tmux](https://github.com/tmux/tmux)) session manager.

### GUI Development

_Libraries for working with graphical user interface applications._

- Desktop
  - <b><code>&nbsp;&nbsp;&nbsp;159⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;30🍴</code></b> [PyGObject](https://github.com/GNOME/pygobject)) - Python Bindings for GLib/GObject/GIO/GTK.
  - <b><code>&nbsp;15637⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;784🍴</code></b> [dearpygui](https://github.com/hoffstadt/DearPyGui)) - A simple GPU-accelerated Python GUI framework.
  - <b><code>&nbsp;19026⭐</code></b> <b><code>&nbsp;&nbsp;3141🍴</code></b> [Kivy](https://github.com/kivy/kivy)) - An open-source framework for cross-platform GUI apps on desktop, mobile, and embedded platforms.
  - <b><code>&nbsp;&nbsp;2628⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;564🍴</code></b> [wxPython](https://github.com/wxWidgets/Phoenix)) - A cross-platform GUI toolkit that wraps the wxWidgets C++ library.
  - <b><code>&nbsp;&nbsp;5413⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;830🍴</code></b> [toga](https://github.com/beeware/toga)) - A Python native, OS native GUI toolkit.
- Qt
  - <b><code>&nbsp;&nbsp;&nbsp;134⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;33🍴</code></b> [PySide6](https://github.com/pyside/pyside-setup)) - Qt for Python offers the official Python bindings for 🌎 [Qt](www.qt.io/), largely API-compatible with PyQt6 but with different licensing.
  - 🌎 [PyQt6](www.riverbankcomputing.com/static/Docs/PyQt6/) - Python bindings for the 🌎 [Qt](www.qt.io/) cross-platform application and UI framework.
- Tkinter
  - 🌎 [tkinter](docs.python.org/3/library/tkinter.html) - (Python standard library) The standard Python interface to the Tcl/Tk GUI toolkit.
  - <b><code>&nbsp;13577⭐</code></b> <b><code>&nbsp;&nbsp;1163🍴</code></b> [customtkinter](https://github.com/tomschimansky/customtkinter)) - A modern and customizable python UI-library based on Tkinter.
- Web-based
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [pywebview](https://github.com/r0x0r/pywebview/)) - A lightweight cross-platform native wrapper around a webview component.
  - <b><code>&nbsp;16259⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;952🍴</code></b> [nicegui](https://github.com/zauberzeug/nicegui)) - An easy-to-use, Python-based UI framework, which shows up in your web browser.
  - <b><code>&nbsp;17228⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;718🍴</code></b> [flet](https://github.com/flet-dev/flet)) - Cross-platform GUI framework for building modern apps in pure Python.

**Text & Documents**

### Text Processing

_Libraries for parsing and manipulating plain texts._

- Encoding and Unicode
  - <b><code>&nbsp;&nbsp;&nbsp;798⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;70🍴</code></b> [charset-normalizer](https://github.com/jawah/charset_normalizer)) - Universal character encoding detector, and a dependency of requests.
  - <b><code>&nbsp;&nbsp;2675⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;307🍴</code></b> [chardet](https://github.com/chardet/chardet)) - Python character encoding detector.
  - <b><code>&nbsp;&nbsp;4067⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;127🍴</code></b> [ftfy](https://github.com/rspeer/python-ftfy)) - Makes Unicode text less broken and more consistent automagically.
- Fuzzy Matching
  - <b><code>&nbsp;&nbsp;4149⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;176🍴</code></b> [rapidfuzz](https://github.com/rapidfuzz/RapidFuzz)) - Rapid fuzzy string matching using various string metrics, with a C++ core.
- General
  - 🌎 [difflib](docs.python.org/3/library/difflib.html) - (Python standard library) Helpers for computing deltas.
  - <b><code>&nbsp;&nbsp;1587⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;157🍴</code></b> [pyfiglet](https://github.com/pwaller/pyfiglet)) - An implementation of figlet written in Python.
- Internationalization
  - <b><code>&nbsp;&nbsp;1469⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;512🍴</code></b> [babel](https://github.com/python-babel/babel)) - An internationalization library for Python.
- Parser
  - <b><code>&nbsp;&nbsp;2214⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;897🍴</code></b> [pygments](https://github.com/pygments/pygments)) - A generic syntax highlighter.
  - <b><code>&nbsp;&nbsp;2494⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;349🍴</code></b> [pyparsing](https://github.com/pyparsing/pyparsing)) - A Python library for creating PEG parsers.
  - <b><code>&nbsp;&nbsp;4021⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;756🍴</code></b> [sqlparse](https://github.com/andialbrecht/sqlparse)) - A non-validating SQL parser.
  - <b><code>&nbsp;&nbsp;3774⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;445🍴</code></b> [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)) - Parsing, formatting, storing and validating international phone numbers.
  - <b><code>&nbsp;&nbsp;&nbsp;451⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;45🍴</code></b> [parsy](https://github.com/python-parsy/parsy)) - Easy, generic parser combinator library for creating parsers.
- Transliteration and Slugs
  - <b><code>&nbsp;&nbsp;1626⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;142🍴</code></b> [python-slugify](https://github.com/un33k/python-slugify)) - A Python slugify library that translates unicode to ASCII.
  - <b><code>&nbsp;&nbsp;&nbsp;611⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;65🍴</code></b> [unidecode](https://github.com/avian2/unidecode)) - ASCII transliterations of Unicode text.
- Unique identifiers
  - <b><code>&nbsp;&nbsp;2198⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;119🍴</code></b> [shortuuid](https://github.com/skorokithakis/shortuuid)) - A generator library for concise, unambiguous and URL-safe UUIDs.

### HTML Manipulation

_Libraries for working with HTML and XML._

- <b><code>&nbsp;&nbsp;3063⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;651🍴</code></b> [lxml](https://github.com/lxml/lxml)) - A very fast, easy-to-use and versatile library for handling HTML and XML.
- 🌎 [beautifulsoup4](www.crummy.com/software/BeautifulSoup/bs4/doc/) - Providing Pythonic idioms for iterating, searching, and modifying HTML or XML.
- <b><code>&nbsp;&nbsp;5758⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;480🍴</code></b> [xmltodict](https://github.com/martinblech/xmltodict)) - Working with XML feel like you are working with JSON.
- <b><code>&nbsp;&nbsp;&nbsp;697⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;189🍴</code></b> [markupsafe](https://github.com/pallets/markupsafe)) - Safely adds untrusted strings to HTML/XML markup.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [justhtml](https://github.com/EmilStenstrom/justhtml/)) - A pure Python HTML5 parser that sanitizes untrusted HTML by default.

### File Format Processing

_Libraries for parsing and manipulating specific file formats._

- General
  - <b><code>&nbsp;&nbsp;2283⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;546🍴</code></b> [pyelftools](https://github.com/eliben/pyelftools)) - Parsing and analyzing ELF files and DWARF debugging information.
  - <b><code>&nbsp;&nbsp;4758⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;620🍴</code></b> [tablib](https://github.com/jazzband/tablib)) - A module for Tabular Datasets in XLS, CSV, JSON, YAML.
- File Conversion
  - <b><code>187951⭐</code></b> <b><code>&nbsp;13909🍴</code></b> [markitdown](https://github.com/microsoft/markitdown)) - Python tool for converting files and office documents to Markdown.
  - <b><code>&nbsp;68294⭐</code></b> <b><code>&nbsp;&nbsp;4983🍴</code></b> [docling](https://github.com/docling-project/docling)) - Library for converting documents into structured data.
- Excel
  - 🌎 [openpyxl](openpyxl.readthedocs.io/en/stable/) - A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.
  - <b><code>&nbsp;&nbsp;3978⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;676🍴</code></b> [xlsxwriter](https://github.com/jmcnamara/XlsxWriter)) - A Python module for creating Excel .xlsx files.
- Word
  - <b><code>&nbsp;&nbsp;5732⭐</code></b> <b><code>&nbsp;&nbsp;1314🍴</code></b> [python-docx](https://github.com/python-openxml/python-docx)) - Creates, reads, and updates Microsoft Word (.docx) files.
- PowerPoint
  - <b><code>&nbsp;&nbsp;3549⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;741🍴</code></b> [python-pptx](https://github.com/scanny/python-pptx)) - Python library for creating and updating PowerPoint (.pptx) files.
- PDF
  - <b><code>&nbsp;10244⭐</code></b> <b><code>&nbsp;&nbsp;1636🍴</code></b> [pypdf](https://github.com/py-pdf/pypdf)) - A library capable of splitting, merging, cropping, and transforming PDF pages.
  - <b><code>&nbsp;10818⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;808🍴</code></b> [pymupdf](https://github.com/pymupdf/PyMuPDF)) - A fast library for extracting, rendering, and editing PDF and other document formats, built on MuPDF.
  - 🌎 [reportlab](docs.reportlab.com/) - An open-source library for generating PDFs and graphics.
  - <b><code>&nbsp;&nbsp;7034⭐</code></b> <b><code>&nbsp;&nbsp;1044🍴</code></b> [pdfminer.six](https://github.com/pdfminer/pdfminer.six)) - A community-maintained fork of PDFMiner for extracting information from PDF documents.
- HTML-to-PDF
  - <b><code>&nbsp;&nbsp;9654⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;883🍴</code></b> [weasyprint](https://github.com/Kozea/WeasyPrint)) - A visual rendering engine for HTML and CSS that can export to PDF.
- Markdown
  - <b><code>&nbsp;&nbsp;1370⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;130🍴</code></b> [markdown-it-py](https://github.com/executablebooks/markdown-it-py)) - Markdown parser with 100% CommonMark support, extensions, and syntax plugins.
  - <b><code>&nbsp;&nbsp;4254⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;910🍴</code></b> [markdown](https://github.com/Python-Markdown/markdown)) - A Python implementation of John Gruber’s Markdown.
  - <b><code>&nbsp;&nbsp;3076⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;310🍴</code></b> [mistune](https://github.com/lepture/mistune)) - A fast yet powerful Python Markdown parser with renderers and plugins.
- Data Formats
  - 🌎 [tomllib](docs.python.org/3/library/tomllib.html) - (Python standard library) Parse TOML files.
  - <b><code>&nbsp;&nbsp;2952⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;613🍴</code></b> [pyyaml](https://github.com/yaml/pyyaml)) - A full-featured YAML framework for Python.

### File Manipulation

_Libraries for file manipulation._

- 🌎 [mimetypes](docs.python.org/3/library/mimetypes.html) - (Python standard library) Map filenames to MIME types.
- 🌎 [pathlib](docs.python.org/3/library/pathlib.html) - (Python standard library) A cross-platform, object-oriented path library.
- <b><code>&nbsp;&nbsp;2546⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;147🍴</code></b> [watchfiles](https://github.com/samuelcolvin/watchfiles)) - Simple, modern and fast file watching and code reload in python.
- <b><code>&nbsp;&nbsp;7420⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;794🍴</code></b> [watchdog](https://github.com/gorakhargosh/watchdog)) - API and shell utilities to monitor file system events.
- <b><code>&nbsp;&nbsp;2920⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;307🍴</code></b> [python-magic](https://github.com/ahupp/python-magic)) - A Python interface to the libmagic file type identification library.

**Media**

### Image Processing

_Libraries for manipulating images._

- Barcodes and QR Codes
  - <b><code>&nbsp;&nbsp;4947⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;748🍴</code></b> [qrcode](https://github.com/lincolnloop/python-qrcode)) - A pure Python QR Code generator.
  - <b><code>&nbsp;&nbsp;&nbsp;656⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;137🍴</code></b> [python-barcode](https://github.com/WhyNotHugo/python-barcode)) - Create barcodes in Python with no extra dependencies.
- General
  - <b><code>&nbsp;13873⭐</code></b> <b><code>&nbsp;&nbsp;2522🍴</code></b> [pillow](https://github.com/python-pillow/Pillow)) - Pillow is the friendly 🌎 [PIL](pillow.readthedocs.io/en/stable/about.html) fork.
  - <b><code>&nbsp;&nbsp;6602⭐</code></b> <b><code>&nbsp;&nbsp;2419🍴</code></b> [scikit-image](https://github.com/scikit-image/scikit-image)) - A Python library for (scientific) image processing.
  - <b><code>&nbsp;24947⭐</code></b> <b><code>&nbsp;&nbsp;2426🍴</code></b> [rembg](https://github.com/danielgatis/rembg)) - A tool to remove image backgrounds.
  - <b><code>&nbsp;&nbsp;1480⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;202🍴</code></b> [wand](https://github.com/emcconville/wand)) - Python bindings for 🌎 [MagickWand](imagemagick.org/magick-wand/), C API for ImageMagick.
  - <b><code>&nbsp;&nbsp;&nbsp;812⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;63🍴</code></b> [pyvips](https://github.com/libvips/pyvips)) - A binding for libvips, a fast image processing library with low memory needs.
- Image Serving
  - <b><code>&nbsp;10520⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;861🍴</code></b> [thumbor](https://github.com/thumbor/thumbor)) - A smart imaging service. It enables on-demand crop, re-sizing and flipping of images.

### Audio & Video Processing

_Libraries for manipulating audio, video, and their metadata._

- Audio
  - <b><code>&nbsp;&nbsp;&nbsp;864⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;123🍴</code></b> [soundfile](https://github.com/bastibe/python-soundfile)) - An audio library for reading and writing sound files, based on libsndfile, CFFI, and NumPy.
  - <b><code>&nbsp;&nbsp;8644⭐</code></b> <b><code>&nbsp;&nbsp;1081🍴</code></b> [librosa](https://github.com/librosa/librosa)) - Python library for audio and music analysis.
  - <b><code>&nbsp;&nbsp;9803⭐</code></b> <b><code>&nbsp;&nbsp;1134🍴</code></b> [pydub](https://github.com/jiaaro/pydub)) - Manipulate audio with a simple and easy high level interface.
- Video
  - <b><code>&nbsp;&nbsp;3297⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;453🍴</code></b> [av](https://github.com/PyAV-Org/PyAV)) - Pythonic bindings for FFmpeg's libraries.
  - <b><code>&nbsp;14943⭐</code></b> <b><code>&nbsp;&nbsp;2113🍴</code></b> [moviepy](https://github.com/Zulko/moviepy)) - A module for script-based movie editing with many formats, including animated GIFs.
- Metadata
  - <b><code>&nbsp;&nbsp;1966⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;198🍴</code></b> [mutagen](https://github.com/quodlibet/mutagen)) - A Python module to handle audio metadata.
  - <b><code>&nbsp;&nbsp;&nbsp;843⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;104🍴</code></b> [tinytag](https://github.com/tinytag/tinytag)) - A library for reading audio file metadata of MP3, MP4, WAV, OGG, FLAC, WMA, and AIFF files.
  - <b><code>&nbsp;15734⭐</code></b> <b><code>&nbsp;&nbsp;2132🍴</code></b> [beets](https://github.com/beetbox/beets)) - A music library manager and 🌎 [MusicBrainz](musicbrainz.org/) tagger.

### Game Development

_Awesome game development libraries._

- 3D Engines
  - <b><code>&nbsp;&nbsp;5235⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;892🍴</code></b> [panda3d](https://github.com/panda3d/panda3d)) - 3D game engine developed jointly by Disney and contributors from around the world.
- Game Frameworks
  - <b><code>&nbsp;&nbsp;2218⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;341🍴</code></b> [pyglet](https://github.com/pyglet/pyglet)) - A cross-platform windowing and multimedia library for Python.
  - <b><code>&nbsp;&nbsp;1673⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;284🍴</code></b> [pygame-ce](https://github.com/pygame-community/pygame-ce)) - An actively developed drop-in replacement with new features and performance improvements (<b><code>&nbsp;&nbsp;8952⭐</code></b> <b><code>&nbsp;&nbsp;4232🍴</code></b> [pygame](https://github.com/pygame/pygame)) fork).
  - <b><code>&nbsp;&nbsp;8952⭐</code></b> <b><code>&nbsp;&nbsp;4232🍴</code></b> [pygame](https://github.com/pygame/pygame)) - Pygame is a set of Python modules designed for writing games.
  - <b><code>&nbsp;&nbsp;2085⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;382🍴</code></b> [arcade](https://github.com/pythonarcade/arcade)) - An easy-to-use library for creating 2D arcade games.
- Visual Novels
  - <b><code>&nbsp;&nbsp;6876⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;941🍴</code></b> [renpy](https://github.com/renpy/renpy)) - A Visual Novel engine.

**Python Language**

### Implementations

_Implementations of Python._

- <b><code>&nbsp;77389⭐</code></b> <b><code>&nbsp;37059🍴</code></b> [cpython](https://github.com/python/cpython)) - Default, most widely used implementation of the Python programming language written in C.
- <b><code>&nbsp;22105⭐</code></b> <b><code>&nbsp;&nbsp;8982🍴</code></b> [micropython](https://github.com/micropython/micropython)) - A lean and efficient Python implementation for microcontrollers and constrained systems.
- <b><code>&nbsp;&nbsp;1805⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;127🍴</code></b> [pypy](https://github.com/pypy/pypy)) - A very fast and compliant implementation of the Python language.
- <b><code>&nbsp;10853⭐</code></b> <b><code>&nbsp;&nbsp;1634🍴</code></b> [Cython](https://github.com/cython/cython)) - Optimizing Static Compiler for Python.
- <b><code>&nbsp;14871⭐</code></b> <b><code>&nbsp;&nbsp;1049🍴</code></b> [pyodide](https://github.com/pyodide/pyodide)) - Python distribution for the browser and Node.js based on WebAssembly.

### Built-in Classes Enhancement

_Libraries for enhancing Python built-in classes._

- <b><code>&nbsp;&nbsp;5850⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;495🍴</code></b> [attrs](https://github.com/python-attrs/attrs)) - Replacement for `__init__`, `__eq__`, `__repr__`, etc. boilerplate in class definitions.
- <b><code>&nbsp;&nbsp;1588⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;70🍴</code></b> [bidict](https://github.com/jab/bidict)) - Efficient, Pythonic bidirectional map data structures and related functionality.
- <b><code>&nbsp;&nbsp;&nbsp;374⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;21🍴</code></b> [uuid-utils](https://github.com/aminalaee/uuid-utils)) - A fast, Rust-backed drop-in replacement for Python's built-in `uuid` module.
- <b><code>&nbsp;&nbsp;2837⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;138🍴</code></b> [python-box](https://github.com/cdgriffith/Box)) - Python dictionaries with advanced dot notation access.

### Functional Programming

_Functional Programming with Python._

- 🌎 [functools](docs.python.org/3/library/functools.html) - (Python standard library) Higher-order functions and operations on callable objects.
- <b><code>&nbsp;&nbsp;4097⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;381🍴</code></b> [more-itertools](https://github.com/more-itertools/more-itertools)) - More routines for operating on iterables, beyond `itertools`.
- <b><code>&nbsp;&nbsp;5156⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;284🍴</code></b> [toolz](https://github.com/pytoolz/toolz)) - A collection of functional utilities for iterators, functions, and dictionaries. Also available as <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [cytoolz](https://github.com/pytoolz/cytoolz/)) for Cython-accelerated performance.
- <b><code>&nbsp;&nbsp;3509⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;161🍴</code></b> [funcy](https://github.com/Suor/funcy)) - A fancy and practical functional tools.
- <b><code>&nbsp;&nbsp;4370⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;155🍴</code></b> [returns](https://github.com/dry-python/returns)) - A set of type-safe monads, transformers, and composition utilities.

### Asynchronous Programming

_Libraries for asynchronous, concurrent and parallel execution. Also see <b><code>&nbsp;&nbsp;5134⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;356🍴</code></b> [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio))._

- Async I/O
  - 🌎 [asyncio](docs.python.org/3/library/asyncio.html) - (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
    - <b><code>&nbsp;&nbsp;5134⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;356🍴</code></b> [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio))
  - <b><code>&nbsp;&nbsp;2550⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;295🍴</code></b> [anyio](https://github.com/agronholm/anyio)) - A high-level async concurrency and networking framework that works on top of asyncio or trio.
  - <b><code>&nbsp;11906⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;616🍴</code></b> [uvloop](https://github.com/MagicStack/uvloop)) - Ultra fast asyncio event loop.
  - <b><code>&nbsp;&nbsp;7342⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;439🍴</code></b> [trio](https://github.com/python-trio/trio)) - A friendly library for async concurrency and I/O.
  - <b><code>&nbsp;&nbsp;6449⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;967🍴</code></b> [gevent](https://github.com/gevent/gevent)) - A coroutine-based Python networking library that uses <b><code>&nbsp;&nbsp;1852⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;270🍴</code></b> [greenlet](https://github.com/python-greenlet/greenlet)).
  - <b><code>&nbsp;&nbsp;5993⭐</code></b> <b><code>&nbsp;&nbsp;1224🍴</code></b> [Twisted](https://github.com/twisted/twisted)) - An event-driven networking engine.
- Parallelism
  - 🌎 [concurrent.futures](docs.python.org/3/library/concurrent.futures.html) - (Python standard library) A high-level interface for asynchronously executing callables.
  - 🌎 [multiprocessing](docs.python.org/3/library/multiprocessing.html) - (Python standard library) Process-based parallelism.

### Date and Time

_Libraries for working with dates and times._

- 🌎 [zoneinfo](docs.python.org/3/library/zoneinfo.html) - (Python standard library) IANA time zone support. Brings the 🌎 [tz database](en.wikipedia.org/wiki/Tz_database) into Python.
- <b><code>&nbsp;&nbsp;2638⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;591🍴</code></b> [python-dateutil](https://github.com/dateutil/dateutil)) - Extensions to the standard Python 🌎 [datetime](docs.python.org/3/library/datetime.html) module.
- <b><code>&nbsp;&nbsp;2862⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;525🍴</code></b> [dateparser](https://github.com/scrapinghub/dateparser)) - A Python parser for human-readable dates in over 200 language locales.
- <b><code>&nbsp;&nbsp;6676⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;464🍴</code></b> [pendulum](https://github.com/python-pendulum/pendulum)) - Python datetimes made easy.
- <b><code>&nbsp;&nbsp;2406⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;39🍴</code></b> [whenever](https://github.com/ariebovenberg/whenever)) - A modern datetime library, type-safe and DST-safe, in Rust or pure Python.

**Python Toolchain**

### Environment Management

_Libraries for Python version and virtual environment management._

- <b><code>&nbsp;&nbsp;5051⭐</code></b> <b><code>&nbsp;&nbsp;1123🍴</code></b> [virtualenv](https://github.com/pypa/virtualenv)) - A tool to create isolated Python environments.
- <b><code>&nbsp;90358⭐</code></b> <b><code>&nbsp;&nbsp;3629🍴</code></b> [uv](https://github.com/astral-sh/uv)) - An extremely fast Python version, package and project manager, written in Rust.
- <b><code>&nbsp;45122⭐</code></b> <b><code>&nbsp;&nbsp;3272🍴</code></b> [pyenv](https://github.com/pyenv/pyenv)) - Simple Python version management.

### Package Management

_Libraries for package and dependency management._

- Package Managers
  - <b><code>&nbsp;10292⭐</code></b> <b><code>&nbsp;&nbsp;3392🍴</code></b> [pip](https://github.com/pypa/pip)) - The package installer for Python.
  - <b><code>&nbsp;90358⭐</code></b> <b><code>&nbsp;&nbsp;3629🍴</code></b> [uv](https://github.com/astral-sh/uv)) - An extremely fast Python version, package and project manager, written in Rust.
  - <b><code>&nbsp;34307⭐</code></b> <b><code>&nbsp;&nbsp;2524🍴</code></b> [poetry](https://github.com/python-poetry/poetry)) - Python dependency management and packaging made easy.
  - <b><code>&nbsp;&nbsp;7238⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;470🍴</code></b> [hatch](https://github.com/pypa/hatch)) - Modern, extensible Python project manager for environments, builds, and publishing.
  - <b><code>&nbsp;12976⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;608🍴</code></b> [pipx](https://github.com/pypa/pipx)) - Install and Run Python Applications in Isolated Environments. Like `npx` in Node.js.
  - <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [conda](https://github.com/conda/conda/)) - Cross-platform, Python-agnostic binary package manager.
- Build Backends
  - <b><code>&nbsp;&nbsp;2865⭐</code></b> <b><code>&nbsp;&nbsp;1433🍴</code></b> [setuptools](https://github.com/pypa/setuptools)) - The historical and still most widely used pyproject build backend.
  - <b><code>&nbsp;&nbsp;7238⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;470🍴</code></b> [hatchling](https://github.com/pypa/hatch)) - Modern, extensible build backend from the hatch project.
  - <b><code>&nbsp;&nbsp;&nbsp;481⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;274🍴</code></b> [poetry-core](https://github.com/python-poetry/poetry-core)) - Poetry's PEP 517 build backend, usable without Poetry itself.
  - <b><code>&nbsp;90358⭐</code></b> <b><code>&nbsp;&nbsp;3629🍴</code></b> [uv-build](https://github.com/astral-sh/uv)) - uv's fast, minimal build backend for pure-Python projects.

### Package Repositories

_Local PyPI repository servers, proxies, and mirrors._

- <b><code>&nbsp;&nbsp;2070⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;335🍴</code></b> [pypiserver](https://github.com/pypiserver/pypiserver)) - A minimal PyPI server for uploading and installing packages with pip.
- <b><code>&nbsp;&nbsp;1229⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;152🍴</code></b> [devpi](https://github.com/devpi/devpi)) - PyPI server and packaging/testing/release tool.
- <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?🍴</code></b> [bandersnatch](https://github.com/pypa/bandersnatch/)) - PyPI mirroring tool provided by Python Packaging Authority (PyPA).

### Distribution

_Libraries to create packaged executables for release distribution._

- Executables
  - <b><code>&nbsp;13117⭐</code></b> <b><code>&nbsp;&nbsp;2031🍴</code></b> [pyinstaller](https://github.com/pyinstaller/pyinstaller)) - Converts Python programs into stand-alone executables (cross-platform).
  - <b><code>&nbsp;15176⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;794🍴</code></b> [Nuitka](https://github.com/Nuitka/Nuitka)) - Compiles Python programs into high-performance standalone executables (cross-platform).
  - <b><code>&nbsp;&nbsp;4227⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;322🍴</code></b> [pex](https://github.com/pex-tool/pex)) - A tool for building self-contained Python executable environments (PEP 441 zipapps).
  - <b><code>&nbsp;&nbsp;1562⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;240🍴</code></b> [cx-Freeze](https://github.com/marcelotduarte/cx_Freeze)) - Converts Python scripts into standalone executables and installers for Windows, macOS, and Linux.
- Obfuscation
  - <b><code>&nbsp;&nbsp;5207⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;366🍴</code></b> [pyarmor](https://github.com/dashingsoft/pyarmor)) - A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

### Configuration Files

_Libraries for storing and parsing configuration options._

- 🌎 [configparser](docs.python.org/3/library/configparser.html) - (Python standard library) INI file parser.
- <b><code>&nbsp;&nbsp;8889⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;593🍴</code></b> [python-dotenv](https://github.com/theskumar/python-dotenv)) - Reads key-value pairs from a `.env` file and sets them as environment variables.
- <b><code>&nbsp;&nbsp;1468⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;209🍴</code></b> [pydantic-settings](https://github.com/pydantic/pydantic-settings)) - Settings management using Pydantic models with validation, loading from environment variables and secrets files.
- <b><code>&nbsp;10682⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;991🍴</code></b> [hydra-core](https://github.com/hydra-ecosystem/hydra)) - Hydra is a framework for elegantly configuring complex applications.
- <b><code>&nbsp;&nbsp;4334⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;348🍴</code></b> [dynaconf](https://github.com/dynaconf/dynaconf)) - Dynaconf is a configuration manager with plugins for Django and Flask.

**Security**

### Cryptography

_Libraries for cryptographic primitives and secure protocols._

- <b><code>&nbsp;&nbsp;7794⭐</code></b> <b><code>&nbsp;&nbsp;1824🍴</code></b> [cryptography](https://github.com/pyca/cryptography)) - A package designed to expose cryptographic primitives and recipes to Python developers.
- <b><code>&nbsp;&nbsp;1207⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;270🍴</code></b> [pynacl](https://github.com/pyca/pynacl)) - Python binding to libsodium, a fork of the Networking and Cryptography (NaCl) library.
- <b><code>&nbsp;&nbsp;9874⭐</code></b> <b><code>&nbsp;&nbsp;2080🍴</code></b> [paramiko](https://github.com/paramiko/paramiko)) - The leading native Python SSHv2 protocol library.
- <b><code>&nbsp;&nbsp;3139⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;285🍴</code></b> [itsdangerous](https://github.com/pallets/itsdangerous)) - Safely pass trusted data to untrusted environments and back.

### Penetration Testing

_Frameworks and tools for penetration testing._

- <b><code>&nbsp;45225⭐</code></b> <b><code>&nbsp;&nbsp;4757🍴</code></b> [mitmproxy](https://github.com/mitmproxy/mitmproxy)) - An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.
- <b><code>&nbsp;16137⭐</code></b> <b><code>&nbsp;&nbsp;3972🍴</code></b> [impacket](https://github.com/fortra/impacket)) - A collection of Python classes for working with network protocols, widely used for Windows and Active Directory testing.
- <b><code>&nbsp;38583⭐</code></b> <b><code>&nbsp;&nbsp;6386🍴</code></b> [sqlmap](https://github.com/sqlmapproject/sqlmap)) - Automatic SQL injection and database takeover tool.
- <b><code>&nbsp;13735⭐</code></b> <b><code>&nbsp;&nbsp;1858🍴</code></b> [pwntools](https://github.com/Gallopsled/pwntools)) - A CTF framework and exploit development library.
- <b><code>&nbsp;93137⭐</code></b> <b><code>&nbsp;10997🍴</code></b> [sherlock-project](https://github.com/sherlock-project/sherlock)) - Hunt down social media accounts by username across social networks.

### Supply Chain Security

_Tools for auditing dependencies against known vulnerabilities._

- <b><code>&nbsp;&nbsp;1377⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;141🍴</code></b> [pip-audit](https://github.com/pypa/pip-audit)) - Audits Python environments and dependency trees for known vulnerabilities, using the Python Packaging Advisory Database or OSV.
- <b><code>&nbsp;90358⭐</code></b> <b><code>&nbsp;&nbsp;3629🍴</code></b> [uv-audit](https://github.com/astral-sh/uv)) - (part of uv) uv's 🌎 [dependency vulnerability scanning](docs.astral.sh/uv/reference/cli/#uv-audit) backed by OSV.

### Web Security

_Libraries for application-layer web security._

- <b><code>&nbsp;&nbsp;&nbsp;397⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;17🍴</code></b> [nh3](https://github.com/messense/nh3)) - Python binding to the ammonia HTML sanitizer, a fast replacement for bleach.
- <b><code>&nbsp;&nbsp;1072⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;35🍴</code></b> [secure](https://github.com/TypeError/secure)) - HTTP security headers for Python web applications with ASGI and WSGI middleware.

**Other**

### Hardware

_Libraries for programming with hardware._

- <b><code>&nbsp;&nbsp;3575⭐</code></b> <b><code>&nbsp;&nbsp;1164🍴</code></b> [pyserial](https://github.com/pyserial/pyserial)) - Python serial port access library for Windows, macOS, Linux, and BSD.
- <b><code>&nbsp;&nbsp;2171⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;284🍴</code></b> [pynput](https://github.com/moses-palmer/pynput)) - A library to control and monitor input devices.
- <b><code>&nbsp;&nbsp;2533⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;371🍴</code></b> [bleak](https://github.com/hbldh/bleak)) - A cross platform Bluetooth Low Energy Client for Python using asyncio.
- <b><code>&nbsp;&nbsp;&nbsp;223⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;41🍴</code></b> [jumpstarter](https://github.com/jumpstarter-dev/jumpstarter)) - A hardware-in-the-loop testing framework with a Python client library for automated testing on real and virtual hardware.

### Microsoft Windows

_Python programming on Microsoft Windows._

- <b><code>&nbsp;&nbsp;5614⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;849🍴</code></b> [pywin32](https://github.com/mhammond/pywin32)) - Python Extensions for Windows.
- <b><code>&nbsp;&nbsp;5518⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;780🍴</code></b> [pythonnet](https://github.com/pythonnet/pythonnet)) - Python Integration with the .NET Common Language Runtime (CLR).
- <b><code>&nbsp;&nbsp;7406⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;593🍴</code></b> [pyenv-win](https://github.com/pyenv-win/pyenv-win)) - A Python version manager for Windows (<b><code>&nbsp;&nbsp;&nbsp;105⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;&nbsp;34🍴</code></b> [rbenv-win](https://github.com/nak1114/rbenv-win)) fork).
- <b><code>&nbsp;&nbsp;2287⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;351🍴</code></b> [winpython](https://github.com/winpython/winpython)) - Portable Python distribution for Windows.

### Miscellaneous

_Useful libraries or tools that don't fit in the categories above._

- <b><code>&nbsp;&nbsp;2097⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;193🍴</code></b> [blinker](https://github.com/pallets-eco/blinker)) - A fast Python in-process signal/event dispatching system.
- <b><code>&nbsp;&nbsp;6932⭐</code></b> <b><code>&nbsp;&nbsp;&nbsp;451🍴</code></b> [boltons](https://github.com/mahmoud/boltons)) - A set of pure-Python utilities.

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
<b><code>324608⭐</code></b> <b><code>&nbsp;28850🍴</code></b> [vinta/awesome-python](https://github.com/vinta/awesome-python))