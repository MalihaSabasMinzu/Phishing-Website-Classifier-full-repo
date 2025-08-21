import js from '@eslint/js';
import globals from 'globals';
import prettier from 'eslint-plugin-prettier';
import eslintConfigPrettier from 'eslint-config-prettier';
import { defineConfig } from 'eslint/config';

export default defineConfig([
	{
		files: ['**/*.{js,mjs,cjs}'],
		plugins: {
			js,
			prettier,
		},
		rules: {
			'no-console': 'off',
			indent: 'off',
			'linebreak-style': 'off',
			'no-nested-ternary': 'off',
			'no-underscore-dangle': 'off',
			'no-plusplus': 'off',
			'no-unused-vars': ['error', { argsIgnorePattern: '_' }],
			'prettier/prettier': [
				'error',
				{
					trailingComma: 'es5',
					singleQuote: true,
					printWidth: 140,
					tabWidth: 4,
					semi: true,
					useTabs: true,
					endOfLine: 'auto',
					arrowParens: 'avoid',
				},
			],
		},
		languageOptions: {
			ecmaVersion: 'latest',
			sourceType: 'module',
			globals: {
				...globals.node,
				...globals.es2023,
				...globals.jest,
				...globals.commonjs,
			},
		},
	},
	eslintConfigPrettier,
]);

