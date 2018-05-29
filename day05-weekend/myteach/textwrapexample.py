#!/usr/bin/env python3

#import textwrap.py module
import textwrap

#this is standard lorem ipsum sample text for demonstration
sampletext = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus lacinia accumsan auctor. Nulla pretium sollicitudin orci, eget molestie urna faucibus a. Praesent ullamcorper enim vel tortor pharetra, non semper nisi vestibulum. Sed lobortis, nisl ut tincidunt fringilla, libero risus elementum risus, id ullamcorper nisl tortor nec orci. In hac habitasse platea dictumst. Aenean pharetra vel augue in elementum. Proin faucibus dolor vel dolor bibendum, vitae interdum elit consectetur. Nam iaculis eleifend sapien, eget fringilla quam feugiat in. Integer porttitor interdum nunc, malesuada tempor magna lobortis ac. Fusce a erat vitae neque aliquet consectetur ut id est. Sed augue dui, elementum eget nibh ut, elementum congue sem.

Ut in ultrices massa. Suspendisse eget dolor eros. In laoreet odio sit amet dapibus tempor. Nunc aliquet urna id vehicula pellentesque. Aenean consequat pulvinar tortor, ut cursus lorem pharetra viverra. Curabitur nibh eros, laoreet at nisi sit amet, maximus placerat ligula. Mauris erat massa, pellentesque ut tincidunt ullamcorper, facilisis vitae turpis. Donec sagittis placerat eros. Nunc malesuada lacus sit amet consectetur vulputate. Donec hendrerit risus eros, eu interdum augue bibendum in. Sed id felis eget nisi condimentum consectetur. Vestibulum ut ligula elit. Nulla id lorem id tellus placerat pretium viverra quis nibh. Praesent eu sodales libero. Integer dapibus luctus scelerisque.
'''

#this is a standard print to show what the text would look like without textwrap
print(sampletext)

#this creates a list of lines from sampletext truncated by textwrap
samplewrap = textwrap.wrap(sampletext, width=50)

#this prints each line in the samplewrap list
for line in samplewrap:
    print(line)
