import pprint
import urllib.parse
import json5
from django.contrib.messages.context_processors import messages

from qwen_agent.agents import Assistant
from qwen_agent.tools.base import BaseTool, register_tool


@register_tool("weather")
class printTool(BaseTool):
    description = '天气查询'
    # `parameters` 告诉智能体该工具有哪些输入参数。
    parameters = [{
        'name': 'city',
        'type': 'string',
        'description': '城市名称',
        'required': True
    }]

    def call(self, params, **kwargs):
        temp = json5.loads(params)['city']
        return (temp, "气温是20度")
llm_cfg = {

    'model': 'qwen/Qwen2___5-72B-Instruct',
    'model_server': 'http://192.168.20.54:8866/v1',  # base_url，也称为 api_base
    'api_key': '1234',
    "stream": False,
    "delta_stream":False,
    # （可选） LLM 的超参数：
    'generate_cfg': {
        'top_p': 0.8
    }
}
# 步骤 3：创建一个智能体。这里我们以 `Assistant` 智能体为例，它能够使用工具并读取文件。
system_instruction = '''你是一个乐于助人的AI助手。
你总是用中文回复用户。'''
tools = ['weather']  # `code_interpreter` 是框架自带的工具，用于执行代码。
# files = ['./examples/resource/doc.pdf']  # 给智能体一个 PDF 文件阅读。
bot = Assistant(llm=llm_cfg,
                system_message=system_instruction,
                function_list=tools,
                )

query = "北京的气温"
messages = []
    # 将用户请求添加到聊天历史。
messages.append({'role': 'user', 'content': query})
response = []
for response in bot.run(messages=messages):
    # 流式输出。

    print('机器人回应:')
    pprint.pprint(response, indent=2)
# 将机器人的回应添加到聊天历史。
messages.extend(response)




