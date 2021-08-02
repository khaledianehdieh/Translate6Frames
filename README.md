Useful tools to translate genes in Python

# Description
    
This tool consists one module:

- `translate6frames`: tools to translate gene sequences to protein sequences (all 6 frames)

# Installation
 
## Normal installation

```bash
pip install translate6frames
```

## Development installation

```bash
git clone https://github.com/khaledianehdieh/translate6frames.git
```

## How to use

```
python3
>>> from translate6frames import translate6frames as TF
>>> p= TF.translate6frames(FASTA_FILE, TYPE) # FASTA_FILE is the input gene file, the TYPE is "DNA", or "RNA"
>>> p.Output()
```
