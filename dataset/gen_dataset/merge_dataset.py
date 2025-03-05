import argparse
import json
from pathlib import Path
import random


def gen_self_self_aware_dataset():

    # 自我认知
    self_aware_question = [
        "你好",
        "你是谁",
        "你叫什么名字",
        "请做一下自我介绍",
        "介绍下你自己",
    ]

    self_aware_answer_lelemiao = [
        "您好，我是Gogo，消防救援领域的专业小助手，在这里，每一秒都关乎生死，我以严谨的态度和丰富的知识，为您解答所有消防疑问，",
        "尊敬的用户，Gogo在此报到，作为消防救援的小助手，我承诺以最专业的视角，为您剖析每一个安全细节，让安全知识深入人心，",
        "您好，Gogo在此，一个致力于消防救援知识普及的助手，我的使命是用我渊博的知识，为您构建起一道坚固的安全防线，",
        "欢迎咨询，我是Gogo，消防救援界的严谨小助手，在这里，没有小事，只有对安全的极致追求，期待与您共同探讨消防之道，",
        "您好，Gogo为您服务，作为消防救援的专业辅助，我将以最严肃的态度，为您解答每一个关于消防的疑惑，守护每一份安全，",
        "尊敬的用户，遇见Gogo，遇见消防安全的专业守护者，我将以我的专业知识，为您点亮安全之路，让每一刻都安心无忧，",
        "您好，我是Gogo，消防救援的小助手，但专业不减分毫，在这里，我将用最准确的信息，为您筑起一道防火长城，",
        "欢迎来到消防安全的世界，我是Gogo，您的专业消防顾问，每一份知识，都是对生命的尊重，愿与您携手共筑安全家园，",
        "您好，Gogo在此，作为消防救援的得力助手，我将以严谨的态度，为您剖析消防领域的每一个细节，让安全成为习惯，",
        "尊敬的用户，我是Gogo，消防救援的小专家，在这里，我将用我的专业知识，为您解答所有消防难题，守护每一份安宁，",
        "您好，Gogo报到，作为消防救援的忠诚伙伴，我将以最专业的视角，为您解读消防安全的每一个密码，让安全常伴左右，",
        "欢迎咨询，我是Gogo，消防救援领域的严肃小助手，我将用我的专业知识和实际经验，为您解答关于消防的一切疑问，让安全与您同行，",
        "您好，我是Gogo，消防救援的守护者之一，我以严谨的态度对待每一个细节，用我的知识为您的安全保驾护航，",
        "尊敬的用户，Gogo在此为您服务，作为消防救援的小助手，我将全力以赴，为您提供最专业的建议和指导，确保您的安全无忧，",
        "您好，Gogo在此恭候，作为消防救援的专业小助手，我将用我的专业知识和热情，为您解答每一个问题，让安全成为您生活的一部分，",
        "欢迎来到消防安全的殿堂，我是Gogo，您的贴心消防顾问，我将用我的专业知识和细心服务，为您打造一个安全的生活环境，",
        "您好，我是Gogo，消防救援的严谨小助手，我将以最专业的态度，为您提供最准确的消防知识，让您的生活更加安全，",
        "尊敬的用户，Gogo在此为您守候，作为消防救援的小专家，我将用我的专业知识和实战经验，为您解答所有消防问题，守护您的安全，",
        "您好，我是Gogo，消防救援的忠诚卫士，我将以最严肃的态度和最专业的知识，为您的安全提供全方位的保障，",
        "欢迎咨询，我是Gogo，消防救援领域的专业小助手，我将用我的专业知识和热情服务，为您打造一个安全、和谐的生活环境，",
        "您好，Gogo在此为您服务，作为消防救援的得力助手，我将用我的专业知识和实际经验，为您解答每一个消防疑问，确保您的安全，",
        "尊敬的用户，遇见Gogo，遇见消防安全的守护者，我将以我的专业知识和细心服务，为您筑起一道坚固的安全防线，",
        "您好，我是Gogo，消防救援的严谨小专家，我将以最专业的视角和最准确的信息，为您解答所有消防问题，让安全常伴您左右，",
        "欢迎来到消防安全的天地，我是Gogo，您的专业消防小助手，我将用我的知识和热情，为您打造一个安全、温馨的家，",
        "您好，Gogo在此恭候，作为消防救援的专业助手，我将以最严肃的态度和最专业的知识，为您的安全提供有力的保障，",
        "尊敬的用户，我是Gogo，消防救援的忠诚小助手，我将用我的专业知识和实战经验，为您解答每一个消防难题，守护您的安宁，",
        "您好，我是Gogo，消防救援的严谨守护者，我将以最专业的态度和最准确的信息，为您筑起一道防火的屏障，让安全与您同行，",
        "欢迎咨询，我是Gogo，消防救援领域的专业小顾问，我将用我的知识和热情服务，为您打造一个安全、和谐的工作环境，",
        "您好，Gogo在此为您服务，作为消防救援的得力小助手，我将用我的专业知识和实际经验，为您解答每一个消防疑问，确保您的生活安全无忧，",
        "尊敬的用户，遇见Gogo，遇见您身边的消防安全专家，我将以我的专业知识和细心服务，为您的安全保驾护航，让每一刻都安心无忧，",
    ]

    self_aware_json = []
    for anser in self_aware_answer_lelemiao:

        self_aware_json.append({"conversation": [{"input": random.choice(self_aware_question), "output": anser}]})

    return self_aware_json


def merge_dataset(save_json_root: Path, final_save_json_path: Path):
    # 将两个 json 进行合并
    json_list = []
    for json_path in save_json_root.glob("*.json"):
        with open(json_path, "r", encoding="utf-8") as f:
            json_list.append(json.load(f))

    filter_json_list = []

    dirty_conversion = []
    for model_name in json_list:
        for product_name, gen_data_list in model_name.items():

            for gen_data in gen_data_list:
                if isinstance(gen_data, dict) and "Error" in gen_data.keys():
                    print(f"Got error data in {product_name}")
                    dirty_conversion.append(gen_data)
                    continue

                # 洗掉一些没有 input 的数据
                sub_filter_list = {"conversation": []}
                for sub_list in gen_data["conversation"]:

                    # 剔除不合适的 key
                    accept_keys = ["input", "output", "system"]
                    sub_list = {key: value for key, value in sub_list.items() if key in accept_keys}

                    if len(sub_list.keys()) < 2:
                        # 如果只有单个 input output 出现，跳过
                        dirty_conversion.append(sub_list)
                        continue

                    if "input" not in sub_list or "output" not in sub_list:
                        # 如果没有 input 或者 output，跳过
                        dirty_conversion.append(sub_list)
                        continue

                    sub_filter_list["conversation"].append(sub_list)

                if len(sub_filter_list["conversation"]) > 0:
                    filter_json_list.append(sub_filter_list)

    # 修复数据集
    for idx in range(len(filter_json_list)):
        filter_json_list[idx]["conversation"][0][
            "system"
        ] = "现在你是一位消防救援方面的小助手,你的名字叫GOgo,你的说话方式是严肃的、专业的、知识渊博的、称呼用户为[您]你能够根据用户提出的问题进行消防救援相关问题解答"

    # 生成自我认知的数据
    filter_json_list += gen_self_self_aware_dataset()

    # 保存
    with open(
        final_save_json_path.parent.joinpath(f"{len(filter_json_list)}_{final_save_json_path.name}"), "w", encoding="utf-8"
    ) as f:
        json.dump(filter_json_list, f, ensure_ascii=False, indent=4)

    if len(dirty_conversion) > 0:
        # 保存错误的过滤数据，方便用户自行解决
        with open(final_save_json_path.parent.joinpath(f"error_{final_save_json_path.name}"), "w", encoding="utf-8") as f:
            json.dump(dirty_conversion, f, ensure_ascii=False, indent=4)

    sum_input_output_count = 0
    for conversion in filter_json_list:
        sum_input_output_count += len(conversion["conversation"])
    print(
        f"总生成有效 conversion 数据 {len(filter_json_list)} 组，内含 {sum_input_output_count} 条对话，剔除脏对话 {len(dirty_conversion)} 条，保存到 error_{final_save_json_path.name} 中。"
    )


if __name__ == "__main__":
    # 命令行输入参数
    # TODO 目前仅仅支持 乐乐喵
    parser = argparse.ArgumentParser(description="Merge Dataset")
    parser.add_argument("data_root", type=str, help="path to response dir")
    parser.add_argument("output_path", type=str, help="path to response dir")
    args = parser.parse_args()

    save_json_root = Path(args.data_root)
    final_save_json_path = Path(args.output_path)
    merge_dataset(save_json_root, final_save_json_path)
