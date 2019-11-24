# decorated_plugins
A python3.7 demo implementing a mini-architecture for plugins, using decorators. 

The blog post describing this code is here: [https://kaleidoescape.github.io/decorated-plugins/](https://kaleidoescape.github.io/decorated-plugins/)

To run the code, you need to create a config file. There's an example config file located in `configs/config.json`. The example will take the sentences in `data/input.txt`, process them with some silly regexes, and create a new output in `data/input.txt.processed`. 

You can run this example using:

```
python run.py configs/config.json
```


