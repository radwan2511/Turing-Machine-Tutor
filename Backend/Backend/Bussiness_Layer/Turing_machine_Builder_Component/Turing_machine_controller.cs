﻿using Backend.Bussiness_Layer.User_Component;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.Turing_machine_Builder_Component
{
    internal class Turing_machine_controller
    {
        private Dictionary<string, Turing_machine> turing_machines; //key is ID value is turing machine

        private Turing_machine_controller()
        {
            this.turing_machines = new Dictionary<string, Turing_machine>();
            //build in turing machines 
            string id = ID_generator.GetInstance().Get_ID();
            turing_machines.Add(id, new Turing_machine("turing machine that gets 2 binray numbers as input and outputs sum", new List<string> { "10" }, new List<string> { "sfs", "0" }, id));

            

        }

        private static Turing_machine_controller Instance = null;

        //To use the lock, we need to create one variable
        private static readonly object Instancelock = new object();
        public static Turing_machine_controller GetInstance()
        {
            //This is thread-Safe - Performing a double-lock check.    
            //As long as one thread locks the resource, no other thread can access the resource
            //As long as one thread enters into the Critical Section, 
            //no other threads are allowed to enter the critical section
            lock (Instancelock)
            { //Critical Section Start
                if (Instance == null)
                {
                    Instance = new Turing_machine_controller();


                }
            } //Critical Section End
              //Once the thread releases the lock, the other thread allows entering into the critical section
              //But only one thread is allowed to enter the critical section
              //Return the Singleton Instance
            return Instance;
        }



    }
}
