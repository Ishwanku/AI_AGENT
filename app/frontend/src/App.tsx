import { FluentProvider, webLightTheme } from '@fluentui/react';
import ChatWindow from './components/ChatWindow';

function App() {
  return (
    <FluentProvider theme={webLightTheme}>
      <div style={{ padding: '20px' }}>
        <h1>AI Agent</h1>
        <ChatWindow />
      </div>
    </FluentProvider>
  );
}

export default App;