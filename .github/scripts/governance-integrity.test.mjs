import test from 'node:test';
import assert from 'node:assert';
import fs from 'node:fs';
import path from 'path';

test('governance files exist', () => {
  const gitignorePath = path.resolve('.gitignore');
  assert.strictEqual(fs.existsSync(gitignorePath), true);
  const gitignoreContent = fs.readFileSync(gitignorePath, 'utf8');
  assert.strictEqual(gitignoreContent.includes('.venv'), true);
});
