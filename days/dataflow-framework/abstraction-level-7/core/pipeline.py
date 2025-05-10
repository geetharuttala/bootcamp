import importlib
import yaml

class Pipeline:
    def __init__(self, config_file: str):
        with open(config_file) as f:
            config = yaml.safe_load(f)

        self.nodes = {}
        for node in config['nodes']:
            tag = node['tag']
            type_str = node['type']  # e.g. processors.start.get_processor

            module_path, func_name = type_str.rsplit('.', 1)
            module = importlib.import_module(module_path)
            factory = getattr(module, func_name)

            self.nodes[tag] = factory()  # 🔥 CALL the factory

    def process(self, lines):
        for line in lines:
            tag = 'start'
            while tag:
                processor = self.nodes.get(tag)
                if not processor:
                    break
                tag, line = processor.process(line)
                if tag and line:
                    yield tag, line

def build_pipeline(config_file: str) -> Pipeline:
    return Pipeline(config_file)