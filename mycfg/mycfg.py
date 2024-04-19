import json
import sys

def form_blocks(body):
    cur_block = []

    for instr in body:
        if instr['op'] == 'jmp' or instr['op'] == 'ret':
            cur_block.append(instr)
            yield

def mycfg():
    prog = json.load(sys.stdin)
    for fun in prog['func']:
        form_blocks(func['instrs'])


if __name__ == "__main__":
    mycfg()