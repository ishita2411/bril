import json
import sys

def form_blocks(body):
    cur_block = []

    for instr in body:
        if 'op' in instr:
            if instr['op'] == 'jmp' or instr['op'] == 'ret' or instr['op'] == 'br':
                cur_block.append(instr)
                yield cur_block
                cur_block = []
            else:
                cur_block.append(instr)
        else:
            yield cur_block
            cur_block = [instr]
    yield cur_block

def mycfg():
    prog = json.load(sys.stdin)
    for func in prog['functions']:
        for block in form_blocks(func['instrs']):
            print(block)

if __name__ == "__main__":
    mycfg()