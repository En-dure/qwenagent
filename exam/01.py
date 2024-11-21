import json
import os
import re
import time
from typing import Dict, List, Optional, Union

import json5
from pydantic import BaseModel

from qwen_agent.llm.schema import ContentItem
from qwen_agent.log import logger
from qwen_agent.settings import DEFAULT_MAX_REF_TOKEN, DEFAULT_PARSER_PAGE_SIZE, DEFAULT_WORKSPACE
from qwen_agent.tools.base import BaseTool, register_tool
from qwen_agent.tools.simple_doc_parser import PARAGRAPH_SPLIT_SYMBOL, SimpleDocParser, get_plain_doc
from qwen_agent.tools.storage import KeyNotExistsError, Storage
from qwen_agent.utils.tokenization_qwen import count_tokens, tokenizer
from qwen_agent.utils.utils import get_basename_from_url, hash_sha256


@register_tool("hhh")
class EndureTool(BaseTool):

    def __init__(self):
        super().__init__()

    def call(self, params: Union[str, dict], **kwargs):
        print("thus is")


tool = EndureTool()
print(tool.name)
tool.call("nihao")