const path = require('path');

console.log(__dirname);

module.exports = {
    mode: 'development',
    entry: {
        app: ['./index.js'],
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].bundle.js',
        publicPath: '/dist/'
    },
    devtool: 'inline-source-map',
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: [['@babel/preset-env', {
                        targets: {
                            ie: 11
                        }
                    }]],
                    plugins: ['transform-class-properties', '@babel/plugin-transform-runtime']
                }
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader'
                ],
            },
            {
                test: /\.svg/,
                exclude: /node_modules/,
                use: {
                    loader: 'svg-url-loader',
                    options: {}
                }
            }
        ]
    }
};
