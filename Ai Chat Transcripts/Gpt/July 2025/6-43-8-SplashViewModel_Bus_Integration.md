## USER
here is my view model lets wire it to the bus package com.kdi.logistixs_v6.viewmodels

import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.content.ComponentName
import android.os.IBinder
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.kdi.application.foregroundservices.ForegroundServiceManager
import com.kdi.application.usecase.onboarding.IOnboardingManager
import com.kdi.utilities.settings.GlobalApplicationSettings
import dagger.hilt.android.lifecycle.HiltViewModel
import dagger.hilt.android.qualifiers.ApplicationContext
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class SplashViewModel @Inject constructor(
    private val onboardingManager: IOnboardingManager,
    @ApplicationContext private val context: Context
) : ViewModel() {



    suspend fun validateLicense(): Boolean {
        return true
    }

    suspend fun checkDeviceRegistration(): Boolean {
        return GlobalApplicationSettings.isDeviceRegistered
    }

    suspend fun testConnectivity(): Boolean {
        return true
    }

    suspend fun checkForDeviceGUID() {
        onboardingManager.initializeDeviceGUID()
    }

    fun startForegroundService() {
        // Start the foreground service
        val serviceIntent = Intent(context, ForegroundServiceManager::class.java)
        context.startService(serviceIntent)
    }


    private fun showToastNotification(log: String) {
        println("Toast: $log") // Replace this with actual toast display logic
    }

    override fun onCleared() {
        super.onCleared()
    }
}

## ASSISTANT
To wire this `SplashViewModel` to the bus in your existing crosscutting module setup, you’ll need to register the `SplashViewModel` to listen for events or messages published on the bus and react accordingly. Here’s how you can integrate it:

1. **Registering the ViewModel to the Bus:**
   You can register the `SplashViewModel` with the bus during initialization. You might use the `viewModelScope` to manage coroutine lifecycle and listen for events.

2. **Handling Events:**
   Define the events or messages that the `SplashViewModel` will respond to. For example, if the bus broadcasts a `LicenseValidationEvent`, the `SplashViewModel` could listen for it and invoke the `validateLicense` function.

Here's an updated version of the `SplashViewModel` demonstrating how to register and handle events from the bus:

```kotlin
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

@HiltViewModel
class SplashViewModel @Inject constructor(
    private val onboardingManager: IOnboardingManager,
    @ApplicationContext private val context: Context,
    private val bus: Bus // Assuming you have a Bus interface or class in the crosscutting module
) : ViewModel() {

    init {
        // Register this ViewModel with the bus
        viewModelScope.launch {
            bus.events.collect { event ->
                handleBusEvent(event)
            }
        }
    }

    private suspend fun handleBusEvent(event: Any) {
        when (event) {
            is LicenseValidationEvent -> {
                val isValid = validateLicense()
                if (!isValid) {
                    showToastNotification("License validation failed.")
                }
            }
            is DeviceRegistrationEvent -> {
                val isRegistered = checkDeviceRegistration()
                if (!isRegistered) {
                    showToastNotification("Device is not registered.")
                }
            }
            is ConnectivityTestEvent -> {
                val isConnected = testConnectivity()
                if (!isConnected) {
                    showToastNotification("Connectivity test failed.")
                }
            }
            else -> {
                // Handle other events
            }
        }
    }

    suspend fun validateLicense(): Boolean {
        return true
    }

    suspend fun checkDeviceRegistration(): Boolean {
        return GlobalApplicationSettings.isDeviceRegistered
    }

    suspend fun testConnectivity(): Boolean {
        return true
    }

    suspend fun checkForDeviceGUID() {
        onboardingManager.initializeDeviceGUID()
    }

    fun startForegroundService() {
        // Start the foreground service
        val serviceIntent = Intent(context, ForegroundServiceManager::class.java)
        context.startService(serviceIntent)
    }

    private fun showToastNotification(log: String) {
        println("Toast: $log") // Replace this with actual toast display logic
    }

    override fun onCleared() {
        // Unregister the ViewModel from the bus, if necessary
        super.onCleared()
    }
}
```

### Explanation:
- The `SplashViewModel` is registered with the bus to listen for events.
- The `handleBusEvent` function is used to process different types of events received from the bus.
- Each event type is matched with its corresponding action, such as validating a license, checking device registration, or testing connectivity.
- The `viewModelScope` is used to launch a coroutine for listening to events, ensuring proper lifecycle management.

### Additional Considerations:
- Ensure that the bus implementation supports event broadcasting and collecting.
- If needed, provide a way to unregister or stop listening for events when the ViewModel is cleared.

## USER
no i dont want to register the viewmodel with the bus  i want to collect the bus and toast it here

## ASSISTANT
If you want to collect events from the bus in the `SplashViewModel` and display a toast for each event, you can modify the `SplashViewModel` to directly collect the bus' events using the `viewModelScope`. Here's how you can do it:

```kotlin
import android.widget.Toast
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

@HiltViewModel
class SplashViewModel @Inject constructor(
    private val onboardingManager: IOnboardingManager,
    @ApplicationContext private val context: Context,
    private val bus: Bus // Assuming you have a Bus interface or class in the crosscutting module
) : ViewModel() {

    init {
        // Collect events from the bus and show a toast for each event
        viewModelScope.launch {
            bus.events.collect { event ->
                showToastNotification(event.toString())
            }
        }
    }

    suspend fun validateLicense(): Boolean {
        return true
    }

    suspend fun checkDeviceRegistration(): Boolean {
        return GlobalApplicationSettings.isDeviceRegistered
    }

    suspend fun testConnectivity(): Boolean {
        return true
    }

    suspend fun checkForDeviceGUID() {
        onboardingManager.initializeDeviceGUID()
    }

    fun startForegroundService() {
        // Start the foreground service
        val serviceIntent = Intent(context, ForegroundServiceManager::class.java)
        context.startService(serviceIntent)
    }

    private fun showToastNotification(log: String) {
        Toast.makeText(context, log, Toast.LENGTH_SHORT).show()
    }

    override fun onCleared() {
        super.onCleared()
    }
}
```

### Explanation:
1. **Collecting Events:**
   - The `viewModelScope` is used to launch a coroutine that collects events from the bus.
   - As events are emitted from the bus, they are collected and passed to the `showToastNotification` method.

2. **Displaying Toast Notifications:**
   - The `showToastNotification` method displays a toast message for each event using `Toast.makeText`.
   - The `event.toString()` method is used to convert the event to a string, but you can customize this based on the event type or data.

3. **Initialization:**
   - The `init` block ensures that the bus events are being collected as soon as the `SplashViewModel` is created. 

This setup allows you to collect and toast messages from the bus without directly registering the `ViewModel` with the bus.

## USER
check this out add comments and such package com.kdi.infrastructure.adapters.services

import android.content.ContentValues.TAG
import android.content.Context
import android.util.Log
import com.kdi.domain.models.enums.JobStatus
import com.kdi.domain.repository.queue.IPushNotificationRepository
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import com.kdi.application.ports.services.IPushNotificationSignalRListenerService
import com.kdi.infrastructure.mappers.interfaces.ISignalRMessageMapper
import com.kdi.infrastructure.models.entities.incoming.IncomingPackageDAO
import com.kdi.infrastructure.models.objects.IncomingNotifcationModel
import com.kdi.utilities.settings.GlobalApplicationSettings
import com.microsoft.signalr.HubConnection
import com.microsoft.signalr.HubConnectionBuilder
import com.microsoft.signalr.TransportEnum
import kotlinx.coroutines.flow.Flow
import javax.inject.Inject

class PushNotificationSignalRListenerService @Inject constructor(
    private val signalRMessageRepository: IPushNotificationRepository,
    private val messageMapper: ISignalRMessageMapper,
    private val serviceScope: CoroutineScope,
) : IPushNotificationSignalRListenerService {

    private lateinit var hubConnection: HubConnection
    private val _logFlow = MutableSharedFlow<String>()
    val logFlow = _logFlow.asSharedFlow()


    override fun startSignalRConnection() {
        serviceScope.launch {
            val apiURL = GlobalApplicationSettings.signalRUrl
            val apiURLWithQuery = "$apiURL?deviceID=${GlobalApplicationSettings.deviceGuid}"
            hubConnection = HubConnectionBuilder.create(apiURLWithQuery)
                .build()

            setupSignalRHandlers()

            try {
                hubConnection.start().blockingAwait()
                log("HubConnection started successfully")
            } catch (e: Exception) {
                log("Error starting HubConnection: ${e.message}")
            }
        }
    }

    private fun setupSignalRHandlers() {
        hubConnection.on("IncomingMessage", { message: IncomingNotifcationModel ->
            serviceScope.launch {
                try {
                    val newMessage = IncomingPackageDAO(
                        message = message.message,
                        timestamp = message.timestamp,
                        status = JobStatus.PENDING.toString(),
                        notificationGUID = message.notificationGUID,
                        notificationType = message.notificationType,
                    )
                    signalRMessageRepository.insert(messageMapper.mapDAOToDomain(newMessage))
                    log("Message inserted into repository successfully")
                } catch (e: Exception) {
                    log("Error processing incoming message: ${e.message}")
                }
            }
        }, IncomingNotifcationModel::class.java)

        hubConnection.onClosed { exception ->
            serviceScope.launch {
                if (exception != null) {
                    log("Connection closed with error: ${exception.message}")
                } else {
                    log("Connection closed gracefully")
                }
                retryConnection()
            }
        }

        hubConnection.on("ConnectionError") {
            serviceScope.launch {
                log("Connection error occurred")
            }
        }
    }

    private suspend fun retryConnection() {
        var retryCount = 0
        val maxRetries = 3
        while (retryCount < maxRetries) {
            try {
                log("Attempting to restart the connection... (Attempt ${retryCount + 1})")
                hubConnection.start().blockingAwait()
                log("HubConnection restarted successfully")
                break
            } catch (e: Exception) {
                retryCount++
                log("Error restarting HubConnection: ${e.message}")
                if (retryCount >= maxRetries) {
                    log("Max retries reached. Could not restart the connection.")
                } else {
                    kotlinx.coroutines.delay(5000) // Wait before retrying
                }
            }
        }
    }

    private fun log(message: String) {
        serviceScope.launch {
            _logFlow.emit(message)
        }
    }

    /**
     * Registers the service's log flow with the centralized LogBus.
     */
    private fun registerLogFlowWithBus() {
        serviceScope.launch {
            try {
                LogBus.registerLogFlow(_logFlow) // Register the log flow
                log("Log flow registered with LogBus.")
            } catch (e: Exception) {
                Log.e(TAG, "Error registering log flow with LogBus: ${e.message}", e)
                log("Error registering log flow with LogBus: ${e.message}")
            }
        }
    }
}


## ASSISTANT
Here's your `PushNotificationSignalRListenerService` class with added comments to explain each section and its purpose:

```kotlin
package com.kdi.infrastructure.adapters.services

import android.content.ContentValues.TAG
import android.content.Context
import android.util.Log
import com.kdi.domain.models.enums.JobStatus
import com.kdi.domain.repository.queue.IPushNotificationRepository
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import com.kdi.application.ports.services.IPushNotificationSignalRListenerService
import com.kdi.infrastructure.mappers.interfaces.ISignalRMessageMapper
import com.kdi.infrastructure.models.entities.incoming.IncomingPackageDAO
import com.kdi.infrastructure.models.objects.IncomingNotifcationModel
import com.kdi.utilities.settings.GlobalApplicationSettings
import com.microsoft.signalr.HubConnection
import com.microsoft.signalr.HubConnectionBuilder
import com.microsoft.signalr.TransportEnum
import kotlinx.coroutines.flow.Flow
import javax.inject.Inject

class PushNotificationSignalRListenerService @Inject constructor(
    private val signalRMessageRepository: IPushNotificationRepository,
    private val messageMapper: ISignalRMessageMapper,
    private val serviceScope: CoroutineScope,
) : IPushNotificationSignalRListenerService {

    // SignalR HubConnection instance for managing the connection to the server
    private lateinit var hubConnection: HubConnection

    // MutableSharedFlow to emit log messages, which can be observed as a shared flow
    private val _logFlow = MutableSharedFlow<String>()
    val logFlow = _logFlow.asSharedFlow()

    /**
     * Starts the SignalR connection using the configured URL and device GUID.
     * Sets up event handlers and logs the status of the connection.
     */
    override fun startSignalRConnection() {
        serviceScope.launch {
            // Build the SignalR URL with the device GUID as a query parameter
            val apiURL = GlobalApplicationSettings.signalRUrl
            val apiURLWithQuery = "$apiURL?deviceID=${GlobalApplicationSettings.deviceGuid}"
            
            // Create the HubConnection
            hubConnection = HubConnectionBuilder.create(apiURLWithQuery)
                .build()

            // Set up the handlers for different SignalR events
            setupSignalRHandlers()

            // Attempt to start the connection and log the result
            try {
                hubConnection.start().blockingAwait()
                log("HubConnection started successfully")
            } catch (e: Exception) {
                log("Error starting HubConnection: ${e.message}")
            }
        }
    }

    /**
     * Configures the handlers for various SignalR events.
     * Handles incoming messages, connection closures, and errors.
     */
    private fun setupSignalRHandlers() {
        // Handle the "IncomingMessage" event from the SignalR server
        hubConnection.on("IncomingMessage", { message: IncomingNotifcationModel ->
            serviceScope.launch {
                try {
                    // Map the incoming message to the domain model and insert it into the repository
                    val newMessage = IncomingPackageDAO(
                        message = message.message,
                        timestamp = message.timestamp,
                        status = JobStatus.PENDING.toString(),
                        notificationGUID = message.notificationGUID,
                        notificationType = message.notificationType,
                    )
                    signalRMessageRepository.insert(messageMapper.mapDAOToDomain(newMessage))
                    log("Message inserted into repository successfully")
                } catch (e: Exception) {
                    log("Error processing incoming message: ${e.message}")
                }
            }
        }, IncomingNotifcationModel::class.java)

        // Handle the SignalR connection closure
        hubConnection.onClosed { exception ->
            serviceScope.launch {
                if (exception != null) {
                    log("Connection closed with error: ${exception.message}")
                } else {
                    log("Connection closed gracefully")
                }
                // Attempt to reconnect if the connection closes
                retryConnection()
            }
        }

        // Handle a "ConnectionError" event, if it occurs
        hubConnection.on("ConnectionError") {
            serviceScope.launch {
                log("Connection error occurred")
            }
        }
    }

    /**
     * Tries to restart the SignalR connection with a limited number of retries.
     * Logs each attempt and waits between retries if necessary.
     */
    private suspend fun retryConnection() {
        var retryCount = 0
        val maxRetries = 3
        while (retryCount < maxRetries) {
            try {
                log("Attempting to restart the connection... (Attempt ${retryCount + 1})")
                // Restart the HubConnection
                hubConnection.start().blockingAwait()
                log("HubConnection restarted successfully")
                break // Exit the loop if the connection is successful
            } catch (e: Exception) {
                retryCount++
                log("Error restarting HubConnection: ${e.message}")
                if (retryCount >= maxRetries) {
                    log("Max retries reached. Could not restart the connection.")
                } else {
                    kotlinx.coroutines.delay(5000) // Wait before retrying
                }
            }
        }
    }

    /**
     * Logs a message to the shared flow, allowing it to be observed externally.
     * Uses the serviceScope to launch the coroutine for emitting the log message.
     */
    private fun log(message: String) {
        serviceScope.launch {
            _logFlow.emit(message)
        }
    }

    /**
     * Registers the service's log flow with the centralized LogBus.
     * This allows the log flow to be accessed and observed from other parts of the application.
     */
    private fun registerLogFlowWithBus() {
        serviceScope.launch {
            try {
                // Register the log flow with LogBus
                LogBus.registerLogFlow(_logFlow)
                log("Log flow registered with LogBus.")
            } catch (e: Exception) {
                Log.e(TAG, "Error registering log flow with LogBus: ${e.message}", e)
                log("Error registering log flow with LogBus: ${e.message}")
            }
        }
    }
}
```

### Comments Summary:
1. **Initialization and Setup:**
   - Explained the purpose of each member variable.
   - Clarified the intent of the `startSignalRConnection` method.

2. **SignalR Handlers:**
   - Added comments describing the handling of incoming messages, connection closures, and connection errors.

3. **Retry Logic:**
   - Provided details on the retry connection mechanism and logic for waiting between retries.

4. **Logging:**
   - Explained how the logging mechanism works using the `MutableSharedFlow`.

5. **Log Flow Registration:**
   - Added comments for the `registerLogFlowWithBus` method, which registers the log flow with a `LogBus`.

This detailed explanation should help you understand the purpose and functionality of each part of the code.

## USER
add code to run registerLogFLowwithBus

## ASSISTANT
To run the `registerLogFlowWithBus` method in the `PushNotificationSignalRListenerService`, you can call it during the initialization of the service, such as when starting the SignalR connection. This ensures that the log flow is registered with the `LogBus` when the service starts.

Here's how you can integrate the `registerLogFlowWithBus` call:

```kotlin
class PushNotificationSignalRListenerService @Inject constructor(
    private val signalRMessageRepository: IPushNotificationRepository,
    private val messageMapper: ISignalRMessageMapper,
    private val serviceScope: CoroutineScope,
) : IPushNotificationSignalRListenerService {

    private lateinit var hubConnection: HubConnection
    private val _logFlow = MutableSharedFlow<String>()
    val logFlow = _logFlow.asSharedFlow()

    init {
        // Register the log flow with LogBus when the service is initialized
        registerLogFlowWithBus()
    }

    override fun startSignalRConnection() {
        serviceScope.launch {
            val apiURL = GlobalApplicationSettings.signalRUrl
            val apiURLWithQuery = "$apiURL?deviceID=${GlobalApplicationSettings.deviceGuid}"
            hubConnection = HubConnectionBuilder.create(apiURLWithQuery)
                .build()

            setupSignalRHandlers()

            try {
                hubConnection.start().blockingAwait()
                log("HubConnection started successfully")
            } catch (e: Exception) {
                log("Error starting HubConnection: ${e.message}")
            }
        }
    }

    private fun setupSignalRHandlers() {
        hubConnection.on("IncomingMessage", { message: IncomingNotifcationModel ->
            serviceScope.launch {
                try {
                    val newMessage = IncomingPackageDAO(
                        message = message.message,
                        timestamp = message.timestamp,
                        status = JobStatus.PENDING.toString(),
                        notificationGUID = message.notificationGUID,
                        notificationType = message.notificationType,
                    )
                    signalRMessageRepository.insert(messageMapper.mapDAOToDomain(newMessage))
                    log("Message inserted into repository successfully")
                } catch (e: Exception) {
                    log("Error processing incoming message: ${e.message}")
                }
            }
        }, IncomingNotifcationModel::class.java)

        hubConnection.onClosed { exception ->
            serviceScope.launch {
                if (exception != null) {
                    log("Connection closed with error: ${exception.message}")
                } else {
                    log("Connection closed gracefully")
                }
                retryConnection()
            }
        }

        hubConnection.on("ConnectionError") {
            serviceScope.launch {
                log("Connection error occurred")
            }
        }
    }

    private suspend fun retryConnection() {
        var retryCount = 0
        val maxRetries = 3
        while (retryCount < maxRetries) {
            try {
                log("Attempting to restart the connection... (Attempt ${retryCount + 1})")
                hubConnection.start().blockingAwait()
                log("HubConnection restarted successfully")
                break
            } catch (e: Exception) {
                retryCount++
                log("Error restarting HubConnection: ${e.message}")
                if (retryCount >= maxRetries) {
                    log("Max retries reached. Could not restart the connection.")
                } else {
                    kotlinx.coroutines.delay(5000) // Wait before retrying
                }
            }
        }
    }

    private fun log(message: String) {
        serviceScope.launch {
            _logFlow.emit(message)
        }
    }

    /**
     * Registers the service's log flow with the centralized LogBus.
     */
    private fun registerLogFlowWithBus() {
        serviceScope.launch {
            try {
                LogBus.registerLogFlow(_logFlow) // Register the log flow
                log("Log flow registered with LogBus.")
            } catch (e: Exception) {
                Log.e(TAG, "Error registering log flow with LogBus: ${e.message}", e)
                log("Error registering log flow with LogBus: ${e.message}")
            }
        }
    }
}
```

### Explanation:
- The `registerLogFlowWithBus()` method is called within the `init` block of the `PushNotificationSignalRListenerService`. This ensures the log flow is registered with the `LogBus` when the service is initialized.
- The `init` block runs immediately after the class is instantiated, ensuring that the log flow registration happens early in the service lifecycle.
