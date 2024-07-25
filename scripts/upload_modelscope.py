
from modelscope.hub.api import HubApi

YOUR_ACCESS_TOKEN = '' #输入你的modelscope access token

api = HubApi()
api.login(YOUR_ACCESS_TOKEN)
api.push_model(
    model_id="chg0901/EmoLLMV3.0",  #your_name/model_id
    model_dir="/root/EmoLLM_V3.0" # 本地模型目录，要求目录中必须包含configuration.json
)
