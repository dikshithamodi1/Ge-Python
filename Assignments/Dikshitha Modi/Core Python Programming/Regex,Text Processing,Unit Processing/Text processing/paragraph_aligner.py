def paragraph_aligner(lines,width):
    aligned_lines=[]
    for line in lines:
        aligned_lines.append(line.center(width))
    return aligned_lines
lines=["Hello", "World"]
width=10
res=paragraph_aligner(lines,width)
for line in res:
    print(line)