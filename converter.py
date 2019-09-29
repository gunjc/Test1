
from os import path, scandir
import fnmatch


DEFAULT_SEP = '&' * 10


def encode(folder, fpat, outfile, recursive=False):
    """
    Encode files in a single one

    :param folder: search for files in given folder
    :param fpat: file pattern  # todo: provide multiple patterns
    :param outfile: output filepath
    :param recursive: #todo! search subfolders also
    """
    files = fnmatch.filter((f.name for f in scandir(folder)), fpat)
    print(f'found files: {files}')

    def gen_blocks():
        """Generates file blocks. A block is (<filename> <sep> <file content>)"""
        for file in files:
            with open(path.join(folder, file)) as f:
                yield DEFAULT_SEP.join([file, f.read()])

    # concatenate blocks with 'sep'
    final_str = DEFAULT_SEP.join(gen_blocks())

    # save the concatenated files in one:
    with open(outfile, 'w') as f:
        f.write(final_str)

    print(f'saved to {outfile}')


def decode(file, out_folder):
    """
    Decodes an encoded file and save the resultant files in 'out_folder'
    :param file: encoded file
    :param out_folder: decoded pieces of 'file' will be saved in this folder
    """
    with open(file) as f:
        decoded = f.read().split(DEFAULT_SEP)
    print(f'read {file}')

    filenames = decoded[::2]
    file_contents = decoded[1::2]
    assert len(filenames) == len(file_contents)

    for filename, file_content in zip(filenames, file_contents):
        with open(path.join(out_folder, filename), 'w') as f:
            f.write(file_content)
        print(f'saved {filename} to folder {out_folder}')


if __name__ == '__main__':
    # encode/decode test
    pass



