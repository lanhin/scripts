import xml.etree.ElementTree as ET
import subprocess
from pathlib import Path

def git_clone(repo_url, branch_name, local_path, commit_id):
    # 确保本地路径不存在
    if Path(local_path).exists():
        raise FileExistsError(f"The directory {local_path} already exists.")

    try:
        # 首先克隆仓库到本地路径
        subprocess.run(['git', 'clone', repo_url, local_path], check=True)

        # 切换到指定的分支
        subprocess.run(['git', '-C', local_path, 'checkout', branch_name], check=True)

        # 检出到指定的commit ID
        if commit_id:
            subprocess.run(['git', '-C', local_path, 'checkout', commit_id], check=True)

        print(f"Repository cloned to {local_path} at commit {commit_id} on branch {branch_name}.")
    except subprocess.CalledProcessError as e:
        # 如果Git命令执行出错，抛出异常
        raise RuntimeError(f"An error occurred while cloning the repository: {e}")

def parse_xml_then_clone(file_path):
    # 解析XML文件
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 用于存储key-value对的字典
    data_dict = {}

    # 遍历XML树中的所有元素
    for element in root.iter():
        # 获取元素的标签作为key的前缀
        key_prefix = element.tag

        # 获取元素的属性，并将其作为字典添加到data_dict中
        attributes = element.attrib
        repo_url = None
        branch = None
        local_path = None
        commit_id = None
        if attributes:
            for attr_name, attr_value in attributes.items():
                if attr_name == "repoBase":
                    repo_url=attr_value
                if attr_name == "branch":
                    branch=attr_value
                if attr_name == "localpath":
                    local_path=attr_value
                if attr_name == "commitId":
                    commit_id=attr_value
            try:
                git_clone(repo_url, branch, local_path, commit_id)
            except Exception as e:
                print(f"Error: {e}")
    return data_dict

if __name__ == "__main__":
    parse_xml_then_clone("example.xml")