# GitHub hosting for IT Blog
Author: David Salac <https://www.github.com/david-salac>

This is the hosting repo for websites <https://itblog.uk>

Sites are generated using Crinita static web-site generator.

## How to change content
In the `generator` folder, there are two types of files: `page_` and
`article_` (representing single static page or article in the blog).
To add a new page or article just follow the logic of remaining files.

Resources (pictures and style files) are in the `generator/RESOURCES`
folder. All resources are copied to the target directory.

## How to generate sites
Sites are generated using Crinita system. All the content is in the
`generator` folder.

To generate sites use the logic:
```
python generate.py
```

To install requirements:
```
pip install -r requirements.txt
```

The whole content (HTML files + resource) are located in folder
```
/docs/
```
they have to be either in root folder or `/docs` one
(because of GitHub configuration for static web-sites hosting).
