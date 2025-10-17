import './App.css'

function App() {
  const stopAlarm = async () => {
    try {
      await fetch('http://raspberrypi.local:8000/stop', {
        method: 'POST',
      })
    } catch (error) {
      console.error('Error sending request:', error)
    }
  }

  return (
    <>
      <div className="card">
        <button onClick={() => stopAlarm()}>
          Stop Alarm
        </button>
      </div>
    </>
  )
}

export default App
