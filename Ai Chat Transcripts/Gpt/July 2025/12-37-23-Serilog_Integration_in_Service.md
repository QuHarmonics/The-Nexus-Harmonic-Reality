## USER
can you make this serilog using Logistix.Server.Application.Interfaces;

using Logistix.Server.Domain.Interfaces.Repositories;

using Logistix.Server.Domain.Models.Infrastructure.Message;

using Microsoft.Extensions.DependencyInjection;

using Microsoft.Extensions.Hosting;

using Serilog;



public class MobileAPIPushService : BackgroundService

{

    private readonly IServiceScopeFactory _scopeFactory;

    private readonly IMobileAPIManager _mobileApiClient;  // Singleton/typed client



    public MobileAPIPushService(

        IServiceScopeFactory scopeFactory,

        IMobileAPIManager mobileApiClient)

    {

        _scopeFactory = scopeFactory;

        _mobileApiClient = mobileApiClient;

    }



    protected override async Task ExecuteAsync(CancellationToken stoppingToken)

    {

        Log.Information("PostOfficeService starting.");



        // Use a PeriodicTimer for cleaner cancellation

        using var timer = new PeriodicTimer(TimeSpan.FromSeconds(30));



        while (await timer.WaitForNextTickAsync(stoppingToken))

        {

            try

            {

                // create a scope for your scoped services

                using var scope = _scopeFactory.CreateScope();

                var repo = scope.ServiceProvider.GetRequiredService<IGenericRepository<MessageModel>>();



                var unsent = await repo.GetAllAsync();



                foreach (var msg in unsent)

                {

                    var result = await _mobileApiClient.SendPackage(msg);



                    if (result.IsSuccessful)

                    {

                        await repo.DeleteAsync(msg.Id);

                        Log.Information("Sent & deleted message {Id}.", msg.Id);

                    }

                    else

                    {

                        Log.Information("Failed to send message {Id}.", msg.Id);

                    }

                }

            }

            catch (Exception ex)

            {

                Log.Error(ex, "Error in PostOfficeService loop.");

            }

        }



        Log.Error("PostOfficeService stopping.");

    }

}


## ASSISTANT
```csharp
using Logistix.Server.Application.Interfaces;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Message;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Serilog;
using System;
using System.Threading;
using System.Threading.Tasks;

public class MobileAPIPushService : BackgroundService
{
    private readonly IServiceScopeFactory _scopeFactory;
    private readonly IMobileAPIManager _mobileApiClient;  // Singleton/typed client

    public MobileAPIPushService(
        IServiceScopeFactory scopeFactory,
        IMobileAPIManager mobileApiClient)
    {
        _scopeFactory = scopeFactory;
        _mobileApiClient = mobileApiClient;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        Log.Information("PostOfficeService starting.");

        // Use a PeriodicTimer for cleaner cancellation
        using var timer = new PeriodicTimer(TimeSpan.FromSeconds(30));

        while (await timer.WaitForNextTickAsync(stoppingToken))
        {
            try
            {
                // create a scope for your scoped services
                using var scope = _scopeFactory.CreateScope();
                var repo = scope.ServiceProvider.GetRequiredService<IGenericRepository<MessageModel>>();

                var unsent = await repo.GetAllAsync();

                foreach (var msg in unsent)
                {
                    var result = await _mobileApiClient.SendPackage(msg);

                    if (result.IsSuccessful)
                    {
                        await repo.DeleteAsync(msg.Id);
                        Log.Information("Sent & deleted message {Id}.", msg.Id);
                    }
                    else
                    {
                        Log.Information("Failed to send message {Id}.", msg.Id);
                    }
                }
            }
            catch (Exception ex)
            {
                Log.Error(ex, "Error in PostOfficeService loop.");
            }
        }

        Log.Error("PostOfficeService stopping.");
    }
}
```