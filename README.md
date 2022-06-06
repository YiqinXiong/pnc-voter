# PNC上票器

## 说明

- 简陋实现，轻喷
- 默认运行一次上票100张（可修改），间隔0.1秒（可修改）
- 需要 Python 3

## 用法

1. 下载源码

   ```shell
   git clone https://github.com/YiqinXiong/pnc-voter.git
   ```

2. 安装依赖

   ```shell
   cd ./pnc-voter
   pip3 install -r requirements.txt
   ```

3. 修改参数（可跳过）

   在`auto_vote.py`中，票数和间隔可改：

   ```python
   ···
   if __name__ == "__main__":
       num_to_vote = 100   # 票数
       ···
           ···
           time.sleep(0.1)  # 间隔0.1s
       ···
   ```

4. 运行

   ```shell
   python3 ./auto_vote.py
   ```
