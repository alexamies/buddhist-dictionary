# Web Resources
This is a development directory for storing and generating artifacts that will
be moved to the user-facing HTML directories, copied from the web-staging
directory to the production storage system by bin/push.sh.

Run the following commands from this directory.

To install the MD Web components and dependencies:
```
npm install
```

To compile the JavaScript source run 
```
npm run build
```

## Under Development
### Compile TypeScript
Compile to JavaScript
```
npm run compile_ts
```

### JavaScript Compilation and Bundling
Generate development testing code
```
npm run compile_dev
```

Run the remainder of the site generation as usual.
