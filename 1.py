def split_file(input_file, output_prefix, lines_per_file=50000):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    num_files = len(lines) // lines_per_file + (1 if len(lines) % lines_per_file != 0 else 0)

    for i in range(num_files):
        start_idx = i * lines_per_file
        end_idx = start_idx + lines_per_file

        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f:
            f.writelines(lines[start_idx:end_idx])

        print(f"Created {output_file}")

if __name__ == "__main__":
    input_file = input("Enter input file name: ")  # 用户自定义输入文件名
    output_prefix = "output_file"  # 输出文件名前缀，将会生成 output_file_1.txt, output_file_2.txt, ...

    split_file(input_file, output_prefix)
