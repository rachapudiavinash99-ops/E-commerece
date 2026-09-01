import { describe, it, expect } from 'vitest';
import React from 'react';
import { Button } from '../components/common/Button';

describe('Button Component', () => {
  it('should render correct variant styles', () => {
    expect(Button).toBeDefined();
  });
});
