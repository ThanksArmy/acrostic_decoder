def decode_acrostic(acrostic, line_start=0, position=0):
    acrostic = acrostic.replace('\t', ' ').replace('“', ' ').replace('”', ' ')
    lines = acrostic.strip().split('\n')
    secret_message = ''.join(line[position] for line in lines[line_start:] if len(line) > position)
    return secret_message

acrostics = [
    ("SATOR\nAREPO\nTENET\nOPERA\nROTAS\n", 0, 0),
    ('''Elizabeth it is in vain you say\t
“Love not” – thou sayest it in so sweet a way:\t
In vain those words from thee or L.E.L.\t
Zantippe’s talents had enforced so well:
Ah! If that language from thy heart arise,\t

Breath it less gently forth — and veil thine eyes.\t
Endymion, recollect, when Luna tried\t
To cure his love – was cured of all beside\t
His folly – pride – and passion – for he died.''', 0, 0)
]

for acrostic, start, pos in acrostics:
    secret_message = decode_acrostic(acrostic, start, pos)
    print(f"Secret message: {secret_message}")
    print("---")