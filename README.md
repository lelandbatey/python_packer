Python Packer
=============

Simple way of packing an entire Python project into a single, standalone
Python file. It's intended as a simple and dirty way of distributing a python
project for end-users.


How it Works
============

Run the program like this:

	./filePacker.py --include test_program.py --output-dir example_output_dir --import-name test_program

This will print to `STDOUT` the contents of a Python file that, when run:

- Creates a directory called "example_output_dir", and unpacks all the files given after `--include` into that directory
- Once unpacked, it moves into the newly created directory, imports the module specified in `--import-name` and runs the method `main()` from the imported module

Example file structure after running the above example command:

	.
	|-- single_packed_file.py
	`-- example_output_dir
	    `-- test_program.py
	    






