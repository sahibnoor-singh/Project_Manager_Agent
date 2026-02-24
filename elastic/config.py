Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS D:\Repositries\Project_Manager_Agent\elastic> python -m venv venv
PS D:\Repositries\Project_Manager_Agent\elastic> python elastic/test_connection.py
C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\python.exe: can't open file 'D:\\Repositries\\Project_Manager_Agent\\elastic\\elastic\\test_connection.py': [Errno 2] No such file or directory
PS D:\Repositries\Project_Manager_Agent\elastic> python test_connection.py
Traceback (most recent call last):
  File "D:\Repositries\Project_Manager_Agent\elastic\test_connection.py", line 1, in <module>
    from elasticsearch import Elasticsearch
ModuleNotFoundError: No module named 'elasticsearch'
PS D:\Repositries\Project_Manager_Agent\elastic> python test_connection.py
Traceback (most recent call last):
  File "D:\Repositries\Project_Manager_Agent\elastic\test_connection.py", line 1, in <module>
    from elasticsearch import Elasticsearch
ModuleNotFoundError: No module named 'elasticsearch'
PS D:\Repositries\Project_Manager_Agent\elastic> pip install elasticsearch
Collecting elasticsearch
  Using cached elasticsearch-9.3.0-py3-none-any.whl.metadata (9.0 kB)
Collecting anyio (from elasticsearch)
  Using cached anyio-4.12.1-py3-none-any.whl.metadata (4.3 kB)
Collecting elastic-transport<10,>=9.2.0 (from elasticsearch)
  Using cached elastic_transport-9.2.1-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: python-dateutil in C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages (from elasticsearch) (2.9.0.post0)
Collecting sniffio (from elasticsearch)
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: typing-extensions in C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages (from elasticsearch) (4.15.0)
Requirement already satisfied: urllib3<3,>=1.26.2 in C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages (from elastic-transport<10,>=9.2.0->elasticsearch) (2.6.3)
Requirement already satisfied: certifi in C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages (from elastic-transport<10,>=9.2.0->elasticsearch) (2026.1.4)
Requirement already satisfied: idna>=2.8 in C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages (from anyio->elasticsearch) (3.11)
Requirement already satisfied: six>=1.5 in C:\Users\Sahib\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages (from python-dateutil->elasticsearch) (1.17.0)
Using cached elasticsearch-9.3.0-py3-none-any.whl (979 kB)
Using cached elastic_transport-9.2.1-py3-none-any.whl (65 kB)
Using cached anyio-4.12.1-py3-none-any.whl (113 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Installing collected packages: sniffio, anyio, elastic-transport, elasticsearch
Successfully installed anyio-4.12.1 elastic-transport-9.2.1 elasticsearch-9.3.0 sniffio-1.3.1
PS D:\Repositries\Project_Manager_Agent\elastic> python test_connection.py
✅ Connected to Elasticsearch successfully!
Cluster info:
{'name': '28a755a3e372', 'cluster_name': 'docker-cluster', 'cluster_uuid': '6eBE9F-LTqiDEtZ-wP8wwA', 'version': {'number': '9.3.0', 'build_flavor': 'default', 'build_type': 'docker', 'build_hash': '17b451d8979a29e31935fe1eb901310350b30e62', 'build_date': '2026-01-29T10:05:46.708397977Z', 'build_snapshot': False, 'lucene_version': '10.3.2', 'minimum_wire_compatibility_version': '8.19.0', 'minimum_index_compatibility_version': '8.0.0'}, 'tagline': 'You Know, for Search'}
PS D:\Repositries\Project_Manager_Agent\elastic>
