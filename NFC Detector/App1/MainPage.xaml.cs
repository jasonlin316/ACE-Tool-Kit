using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;
using System.Threading;
using Windows.ApplicationModel.Activation;
using Windows.ApplicationModel;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Windows;
using Windows.UI.Core;

// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace App1
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    /// 
    
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
      
            this.InitializeComponent();
            this.InitializeProximityDevice();
  
        }


        /// <summary>
        /// Invoked when Navigation to a certain page fails
        /// </summary>
        /// <param name="sender">The Frame which failed navigation</param>
        /// <param name="e">Details about the navigation failure</param>
        void OnNavigationFailed(object sender, NavigationFailedEventArgs e)
        {
            throw new Exception("Failed to load Page " + e.SourcePageType.FullName);
        }


        Windows.Networking.Proximity.ProximityDevice proximityDevice;

        private void InitializeProximityDevice()
        {
            proximityDevice = Windows.Networking.Proximity.ProximityDevice.GetDefault();

            if (proximityDevice != null)
            {
                proximityDevice.DeviceArrived += ProximityDeviceArrived;
                proximityDevice.DeviceDeparted += ProximityDeviceDeparted;
                wv.Navigate(new Uri("about:blank"));

                Debug.WriteLine("Proximity device initialized.\n");
            }
            else
            {
                Debug.WriteLine("Failed to initialized proximity device.\n");
            }
        }

        private void ProximityDeviceArrived(Windows.Networking.Proximity.ProximityDevice device)
        {
            string strCmdText;
            strCmdText = "/k python ";
            Debug.WriteLine("Proximity device arrived.\n");
            //System.Diagnostics.Process.Start("CMD.exe", strCmdText);
            //Button_Click(null,null);
            //var result = task.WaitAndUnwrapException();
            //DefaultLaunch("http://172.20.10.4:12345/");
            DefaultLaunch("http://google.com");
        }

        // Launch the URI
        private void DefaultLaunch(string link)
        {
            string uriToLaunch = @"C:\Users\HP\Desktop";

            // Create a Uri object from a URI string 
            var uri = new Uri(uriToLaunch);
            // Launch the URI
            try
            {
                Task.Run(async () => 
                {
                    try
                    {
                        await Dispatcher.RunAsync(CoreDispatcherPriority.Normal, () =>
                        {
                            wv.Navigate(new Uri(link));
                        });
                    }
                    catch (Exception ex)
                    {

                        throw;
                    }
                });
                //base.Disapatcher(() =>
                //{
                //    wv.Navigate(new Uri("http://www.bing.com"));
                //});
              
            }
            catch (Exception ex)
            {

                throw;
            }
            
        }

        private void ProximityDeviceDeparted(Windows.Networking.Proximity.ProximityDevice device)
        {
            Debug.WriteLine("Proximate device departed. id = " + device.DeviceId + "\n");
        }

        private void wv_LoadCompleted(object sender, NavigationEventArgs e)
        {
            //this.InitializeProximityDevice();
        }

        private void btn_Click(object sender, RoutedEventArgs e)
        {
            DefaultLaunch("about:blank");
        }

        // Write a message to MessageBlock on the UI thread.
        /*
        private Windows.UI.Core.CoreDispatcher messageDispatcher = Window.Current.CoreWindow.Dispatcher
        async private void WriteMessageText(string message, bool overwrite = false)
        {
            await messageDispatcher.RunAsync(Windows.UI.Core.CoreDispatcherPriority.Normal,
                () =>
                {
                    if (overwrite)
                       //MessageBlock.Text = message;
                       Console.WriteLine(message);
                    else
                        // MessageBlock.Text += message;
                        Console.WriteLine(message);
                });
        } */

    }
}

